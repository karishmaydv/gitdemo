from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.maximize_window()
time.sleep(2)

# Take screenshot
driver.save_screenshot("google_homepage.png")

print("Screenshot captured successfully")

driver.quit()

#screenshots of particular elements
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

driver.maximize_window()
time.sleep(2)

# Locate element
search_box = driver.find_element(By.NAME, "q")

# Take screenshot of element
search_box.screenshot("search_box.png")

print("Element screenshot captured")

driver.quit()
'''