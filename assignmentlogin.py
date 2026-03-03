'''
2. Login Form Automation
Site: https://practicetestautomation.com/practice-test-login/
Credentials:
● Username: student
● Password: Password123
Tasks You Can Perform:
● Validate redirection to the secure area
● Confirm visibility of Log out button after login
● Test negative scenarios with invalid credentials
'''

from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("student")
driver.find_element(By.ID,"password").send_keys("Password123")
driver.find_element(By.ID,"submit").click()
#for logout button visibility without wait

logout_button = driver.find_element(By.LINK_TEXT, "Log out")
#logout_button= driver.find_element(By.CLASS_NAME,"wp-block-button__link has-text-color has-background has-very-dark-gray-background-color")

if logout_button.is_displayed():
    print("Logout button is visible")
    # with explict wait for logut button visibility

wait =WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))