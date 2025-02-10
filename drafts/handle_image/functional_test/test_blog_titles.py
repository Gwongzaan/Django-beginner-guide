from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

import unittest
from pathlib import Path

# installation path of the chrome driver
install_path = Path(__file__).resolve().parent.parent.parent
cache_manager = DriverCacheManager(install_path)
chrome_options = Options()
chrome_options.add_argument('--headless')

class BlogTitlesTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(
            service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
            options=chrome_options
        )

    def tearDown(self):
        self.browser.quit()

    def test_can_retrieve_a_list_of_blogs(self):
        # user checkout the blog
        self.browser.get("http://localhost:8000/blog")
        # user see the page title
        self.assertIn("Titles", self.browser.title.strip())
        # user see a list of titles of blogs
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text.strip()
        self.assertIn('List of Blogs', header_text)
        list_of_blog_titles = self.browser.find_element(By.ID, 'list_of_blog')
        rows = list_of_blog_titles.find_elements(By.TAG_NAME, 'li')
        for row in rows:
            a = row.find_element(By.TAG_NAME, 'a')
            print(a.text)

        ####################
        ####################
        ####################
        ####################

        self.fail('Finish the test!')

        ####################
        ####################
        ####################
        ####################

        # user click a listed item

        # user see detail content of the blog: title, author, published date, content

        # user quit browsing

    

if __name__ == "__main__":
    unittest.main(warnings='ignore')
