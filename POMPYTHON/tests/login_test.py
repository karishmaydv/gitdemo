import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
from ..pages.login_pages import LoginPage # import the pages login page clas to test class

@pytest.fixture()

def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("username,password")



def test_login(driver):
    login_page = LoginPage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/index.html")
    time.sleep(2)
    login_page.enter_username("Test")
    time.sleep(2)
    login_page.password_textbox("Test")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)
    


    # driver.get("https://trytestingthis.netlify.app/index.html")
    # username_field = driver.find_element(By.ID,"uname")
    # password_field = driver.find_element(By.ID,"pwd")
    # submit_button  = driver.find_element(By.XPATH,"//input[@value='Login']")
    #
    # username_field.send_keys()
    # password_field.send_keys()
    # time.sleep(2)
    # submit_button.click()
    assert "Successful" in driver.page_source
    time.sleep(2)
