from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(5)
# Login
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit']").click()

time.sleep(5)

# Navigate to PIM module
driver.find_element(By.XPATH, "//span[text()='PIM']").click()
time.sleep(3)

# Click dropdown (Example: Employment Status)
dropdown = driver.find_element(By.XPATH, "//label[text()='Employment Status']/../following-sibling::div//div[contains(@class,'select-text')]")
dropdown.click()
time.sleep(2)

# Select option from dropdown list
option = driver.find_element(By.XPATH, "//span[text()='Full-Time Permanent']")
option.click()

time.sleep(3)

driver.quit()