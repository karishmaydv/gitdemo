#simple alerts and popup

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

# Click simple alert button
driver.find_element(By.ID, "alertButton").click()

# Switch to alert
alert = driver.switch_to.alert

# Print alert text
print(alert.text)

# Accept alert
alert.accept()

time.sleep(2)
driver.quit()

#Task2: Click confirm box → Accept or dismiss → Verify result.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

# Click confirm alert
driver.find_element(By.ID, "confirmButton").click()

alert = driver.switch_to.alert

# Accept alert
alert.accept()

# OR dismiss
# alert.dismiss()

# Verify result message
result = driver.find_element(By.ID, "confirmResult").text
print(result)

time.sleep(2)
driver.quit()
#task 3 Task: Enter text → Accept → Verify response. prompt box
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://demoqa.com/alerts")

# Click prompt alert
driver.find_element(By.ID, "promtButton").click()

alert = driver.switch_to.alert

# Enter text
alert.send_keys("Selenium Python Test")

# Accept alert
alert.accept()

# Verify response
result = driver.find_element(By.ID, "promptResult").text
print(result)

time.sleep(2)
driver.quit()