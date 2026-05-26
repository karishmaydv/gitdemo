from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")

wait = WebDriverWait(driver, 10)

# -----------------------------
# Select State
# -----------------------------
state_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "state"))).click()

#state_dropdown.click()

state_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='NCR']"))).click

#state_option.click()

# -----------------------------
# Select City
# -----------------------------
city_dropdown = wait.until(
    EC.element_to_be_clickable((By.ID, "city"))
)
city_dropdown.click()

city_option = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[text()='Delhi']"))
)
city_option.click()

# -----------------------------
# Select Hobbies Checkboxes
# -----------------------------
sports_checkbox = driver.find_element(By.XPATH, "//label[text()='Sports']")
reading_checkbox = driver.find_element(By.XPATH, "//label[text()='Reading']")
music_checkbox = driver.find_element(By.XPATH, "//label[text()='Music']")

sports_checkbox.click()
reading_checkbox.click()
music_checkbox.click()

# -----------------------------
# Assertions (Validation)
# -----------------------------

# Validate checkboxes selected
sports_input = driver.find_element(By.ID, "hobbies-checkbox-1")
reading_input = driver.find_element(By.ID, "hobbies-checkbox-2")
music_input = driver.find_element(By.ID, "hobbies-checkbox-3")

assert sports_input.is_selected(), "Sports not selected"
assert reading_input.is_selected(), "Reading not selected"
assert music_input.is_selected(), "Music not selected"

# Validate State & City text
selected_state = driver.find_element(By.ID, "state").text
selected_city = driver.find_element(By.ID, "city").text

assert "NCR" in selected_state, "State not selected properly"
assert "Delhi" in selected_city, "City not selected properly"

print("✅ Dropdown and Checkbox validations passed")

driver.quit()