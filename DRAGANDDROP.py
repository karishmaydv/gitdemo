import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/droppable")

wait = WebDriverWait(driver, 10)

# Locate elements
#source = wait.until(EC.visibility_of_element_located((By.ID, "draggable"))) # DRAG
#target = wait.until(EC.visibility_of_element_located((By.ID, "droppable")))

source = wait.until(EC.presence_of_element_located((By.ID, "draggable")))
target = wait.until(EC.presence_of_element_located((By.ID, "droppable")))
# Perform Drag and Drop

actions = ActionChains(driver)
#actions.click_and_hold(source).move_to_element(target).release().perform()
actions.drag_and_drop(source, target).perform()

# Validation
result = target.text
print("Result:", result)
time.sleep(5)
assert result == "Dropped!"
print("✅ Drag and Drop Successful")

driver.quit()