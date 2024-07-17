from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import os
import time
import sys

def test():
    tor_firefox = os.environ["TOR_FIREFOX_PATH"]
    profile_path = os.environ["DEFAULT_PROFILE"]

    options = Options()
    options.binary_location = tor_firefox
    options.add_argument("--profile")
    options.add_argument(profile_path)
    # options.add_argument("--headless")

    os.environ['MOZ_REMOTE_SETTINGS_DEVTOOLS'] = '1'
    driver = webdriver.Firefox(options=options)

    print("Starting Webscraper")

    while(1):
        print("Connecting to Tor...")
        if driver.title== "":
            break
        time.sleep(1)
    
    driver.get("https://check.torproject.org")
    
    time.sleep(0)
    
    driver.quit()
    sys.exit()


