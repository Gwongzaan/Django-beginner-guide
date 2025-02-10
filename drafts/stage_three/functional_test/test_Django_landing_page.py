from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.driver_cache import DriverCacheManager
from selenium.webdriver.chrome.options import Options

from pathlib import Path
# installation path of the chrome driver
install_path = Path(__file__).resolve().parent.parent.parent
cache_manager = DriverCacheManager(install_path)
chrome_options = Options()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(
    service=Service(ChromeDriverManager(cache_manager=cache_manager).install()),
    options=chrome_options
)

# testng the isntallation of Django by checking if the title contains 
# "The install worked successfully!"
browser.get("http://localhost:8000")
assert "The install worked successfully!" in browser.title
