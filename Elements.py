from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")
# googleSearchBox = driver.find_element(By.ID,"APjFqb")
# googleSearchBox.send_keys("Automation")
# #driver.find_element(By.NAME,"btnK").click() this is for inspect element and click method
#
# # press the enter key for google search from keyboard
# googleSearchBox.send_keys(Keys.RETURN)
# time.sleep(2)

driver.get("https://trytestingthis.netlify.app/index.html")
driver.find_element(By.ID,"fname").send_keys("Karishma")
driver.find_element(By.ID,"lname").send_keys("Yadav")
time.sleep(2)
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click() #this is the relative xpath when no other locators is given
time.sleep(2)