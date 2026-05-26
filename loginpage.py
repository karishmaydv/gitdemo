#automate any url from scratch..

from  selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")


driver.find_element(By.ID,"_R_1h6kqsqppb6amH1_").send_keys("9981877388")
driver.find_element(By.ID,"_R_1hmkqsqppb6amH1_").send_keys(123)
driver.find_element(By.XPATH,"//div[@role='button']")
