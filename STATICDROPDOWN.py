import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#url
#https://rahulshettyacademy.com/angularpractice/

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")


#STATIC DROPDOWN
dropdown= Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
time.sleep(10)
dropdown.select_by_index(1)
#dropdown.select_by_visible_text("female")



