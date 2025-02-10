from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException

import time
import unittest
from pathlib import Path

from lists.models import Item

# installation path of the chrome driver
install_path = Path(__file__).resolve().parent.parent.parent
cache_manager = DriverCacheManager(install_path)
chrome_options = Options()
chrome_options.add_argument('--headless')

MAX_WAIT = 10

class NewVistorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
            options=chrome_options
        )

    def tearDown(self):
        self.browser.quit()

    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time  > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element(By.ID, 'id_list_table')
        rows = table.find_elements(By.TAG_NAME, 'tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # user checkout the blog
        self.browser.get(self.live_server_url)
        # user see the page title
        self.assertIn("To-Do lists", self.browser.title)
        # user see a list of titles of blogs
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text.strip()
        self.assertIn('Your To-Do list', header_text)
        # user enter a to-do item 
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')
        # user types "Buy books" into a text box
        inputbox.send_keys('Buy books')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.wait_for_row_in_list_table('1: Buy books')

        # suer type another to-do
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Read the book')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        self.wait_for_row_in_list_table('1: Buy books')
        self.wait_for_row_in_list_table('2: Read the book')

    def test_multiple_users_can_start_lists_at_different_urls(self):
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Buy books')
        inputbox.send_keys(Keys.ENTER)
        items = Item.objects.all()
        self.wait_for_row_in_list_table("1: Buy books")

        # user see that her to-do ist has a unique URL
        user1_url = self.browser.current_url
        self.assertRegex(user1_url, '/lists/.+')

        self.browser.quit()

        # user2 visits the home page , there is no sign of user1's list
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
            options=chrome_options
        )
        self.browser.get(self.live_server_url)
        # another user start a new list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy books', page_text)
        self.assertNotIn('read books', page_text)
        inputbox = self.browser.find_element(By.ID, "id_new_item")
        inputbox.send_keys('Buy MILK')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy MILK')
        # user2 gets his own unique URL
        user2_url = self.browser.current_url
        self.assertRegex(user2_url, '/lists/.+')
        self.assertNotEqual(user2_url, user1_url)

        # there's not trace of user1's list
        page_text = self.browser.find_element(By.TAG_NAME, 'body').text
        self.assertNotIn('Buy books', page_text)
        self.assertIn('Buy MILK', page_text)
