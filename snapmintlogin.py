from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.common.by import time
import time


driver = webdriver.Chrome()
driver.get("https://snapmint.com/") #open the current url
time.sleep(2)

# for signup
#driver.find_element(By.NAME,"mobile").send_keys("9981877388")
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Enter Mobile Number']").send_keys("9981877388")
#for otp
driver.find_element(By.CSS_SELECTOR,"button[type='button']").click()

