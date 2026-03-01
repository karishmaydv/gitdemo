import selenium
from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
#from selenium.webdriver.common.keys import keys
from selenium.webdriver import Keys

# install_chromedriver()
# driver = selenium.webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(90)

#web = webdriver.Chrome("C:\Users\Dell Latitude\Downloads\chromedriver_win32")
web = webdriver.Chrome(ChromeDriverManager().install())
web.get("https://snapmint:ciHns$@NKSa@qa2.snapmint.com/merchant-demo")
time.sleep(2)

mobilenumber_field = web.find_element(By.ID,"new-mobile").clear() # driver name i put web in webdriver chrome
mobilenumber_field.send_keys("9981877388")
merchant_id = web.find_element(By.NAME, "merchant_id").clear()
merchant_id.send_keys("1453")
time.sleep(2)
store_id = web.find_element(By.NAME, "store_id")
order_id = web.find_element(By.NAME, "order_id")
order_value = web.find_element(By.NAME, "order_value").clear()
order_value.send_keys("1000")
full_name = web.find_element(By.NAME, "full_name").clear()
full_name.send_keys("Karishma")
email_id = web.find_element(By.NAME, "email").clear()
email_id.send_keys("kari39@gmail.com")
city = web.find_element(By.NAME, "shipping_city")
zip_code = web.find_element(By.NAME, "shipping_zip")
checksum_value = web.find_element(By.NAME, "checksum_hash").send_keys(1)
web.implicitly_wait(10)
createchecksum_button = web.find_element(By.ID, "checksum_btn").click()


