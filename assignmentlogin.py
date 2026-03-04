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

logout_button = driver.find_element(By.LINK_TEXT, "Log out") # link is present..

# with explict wait for logut button visibility for specific logout button
wait = WebDriverWait(driver, 10)
Logout_button =wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))

# Confirm it is displayed
if logout_button.is_displayed():
    print("Logout button is visible")

#2.Validate redirection to the secure area
#validate using url
#explicit wait used

wait = WebDriverWait(driver, 10)

# Wait until URL contains expected text
wait.until(EC.url_contains("logged-in-successfully"))

current_url = driver.current_url

if "logged-in-successfully" in current_url:
    print("✅ Successfully redirected to Secure Area")
else:
    print("❌ Redirection failed")

#3. validate negative tc with invalid creds
driver.get("https://practicetestautomation.com/practice-test-login/")
driver.find_element(By.ID,"username").send_keys("karishma")
driver.find_element(By.ID,"password").send_keys("123")
driver.find_element(By.ID,"submit").click()
wait = WebDriverWait(driver,5)
#validate error message
error_message =wait.until(EC.visibility_of_element_located((By.ID,"error")))
if error_message.is_displayed():
    print("Your username is invalid!")
