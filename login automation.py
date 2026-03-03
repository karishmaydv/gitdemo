from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# Setup WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# URL
url = "https://practicetestautomation.com/practice-test-login/"
driver.get(url)

wait = WebDriverWait(driver, 10)

def valid_login_test():
    print("Running Positive Login Test...")

    # Locate elements
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    submit_btn = driver.find_element(By.ID, "submit")

    # Enter valid credentials
    username.clear()
    username.send_keys("student")

    password.clear()
    password.send_keys("Password123")

    submit_btn.click()

    try:
        # Validate redirection to secure area
        wait.until(EC.url_contains("logged-in-successfully"))
        print("✅ Redirected to Secure Area")

        # Validate Logout button visibility
        logout_btn = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Log out"))
        )

        if logout_btn.is_displayed():
            print("✅ Logout button is visible")

    except TimeoutException:
        print("❌ Positive login test failed")

    print("-" * 50)


def invalid_login_test():
    print("Running Negative Login Test...")

    driver.get(url)

    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    submit_btn = driver.find_element(By.ID, "submit")

    # Enter invalid credentials
    username.clear()
    username.send_keys("wronguser")

    password.clear()
    password.send_keys("wrongpassword")

    submit_btn.click()

    try:
        error_message = wait.until(
            EC.visibility_of_element_located((By.ID, "error"))
        )

        if error_message.is_displayed():
            print("✅ Error message displayed for invalid login")

    except TimeoutException:
        print("❌ Negative login test failed")

    print("-" * 50)


# Execute Tests
valid_login_test()
invalid_login_test()

# Close browser
time.sleep(3)
driver.quit()