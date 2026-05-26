from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://snapmint.com/")
driver.maximize_window()

wait = WebDriverWait(driver,10) #explicitwait 

# click signup
signup = wait.until(
    EC.element_to_be_clickable((By.XPATH,"//button[text()='Sign-up']"))
)
signup.click()

# enter mobile
mobile = wait.until(
    EC.visibility_of_element_located((By.NAME,"mobile"))
)
mobile.send_keys("9981877388")

# click get otp
otp = driver.find_element(By.XPATH,"//button[contains(text(),'OTP')]")
otp.click()