import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

driver.find_element(By.ID,"state").click()
#driver.find_element(By.XPATH,"//div[contains(text(),'Select State')").click()
time.sleep(5)

# Select value
driver.find_element(By.XPATH, "//div[text()='NCR']").click()