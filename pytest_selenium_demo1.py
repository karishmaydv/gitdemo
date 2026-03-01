import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

@pytest.fixture()

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()



def test_google_search(driver): # pytest function should start with test so it will test_google_search
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://google.com")
    googleSearchBox = driver.find_element(By.ID,"APjFqb")
    googleSearchBox.send_keys("Automation")
    #driver.find_element(By.NAME,"btnK").click() this is for inspect element and click method

    # press the enter key for google search from keyboard
    googleSearchBox.send_keys(Keys.RETURN)
    time.sleep(2)
   # driver.close()
   # driver.quit()
    print("Test Completed")