import time
import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from chromedriver_autoinstaller import install as install_chromedriver

# this is the correct file running the merchant demo page.

# Initialize WebDriver
driver = webdriver.Chrome()

driver.get("https://snapmint:ciHns$@NKSa@qa2.snapmint.com/merchant-demo")
time.sleep(2)

mobilenumber_field = driver.find_element(By.ID, "new-mobile")
mobilenumber_field.clear()
mobilenumber_field.send_keys("9981877388")

merchant_id = driver.find_element(By.NAME, "merchant_id")
merchant_id.clear()
merchant_id.send_keys("1453")

time.sleep(2)

order_value = driver.find_element(By.NAME, "order_value")
order_value.clear()
order_value.send_keys("1000")

full_name = driver.find_element(By.NAME, "full_name")
full_name.clear()
full_name.send_keys("Karishma")

email_id = driver.find_element(By.NAME, "email")
email_id.clear()
email_id.send_keys("kari39@gmail.com")

city = driver.find_element(By.NAME, "shipping_city")
zip_code = driver.find_element(By.NAME, "shipping_zip")

checksum_value = driver.find_element(By.NAME, "checksum_hash")
checksum_value.send_keys("1")

createchecksum_button = driver.find_element(By.ID, "checksum_btn").click()