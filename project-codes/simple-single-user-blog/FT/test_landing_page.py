from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(service=Service(), options=chrome_options)
# testng the isntallation of Django by checking if the title contains 
# "The install worked successfully!"
browser.get("http://localhost:8000")
assert "The install worked successfully!" in browser.title
# fail on purpose, make sure the Selenium is setup correctly
assert "The install worked successfullly!" in browser.title
