import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")
'''
#simple alert
#driver.find_element(By.ID,"alertBtn").click()
# wait because it will quickly open
time.sleep(5)

alert = driver.switch_to.alert

#print("alert text:"+alert.text) # for alert text

#driver.switch_to.alert.accept() # for ok button
'''
'''
#confirmation alert
driver.find_element(By.ID,"confirmBtn").click() # find button and click
alert= driver.switch_to.alert
print("alert text:"+alert.text) # for alert text
#driver.switch_to.alert.accept()# for ok button
driver.switch_to.alert.dismiss() # for cancel button
# this will user for print after alet button succesfully clik  message

result = driver.find_element(By.ID, "demo").text
print(result)
'''

#prompt alert
driver.find_element(By.ID,"promptBtn").click()
time.sleep(5)
alert= driver.switch_to.alert
alert.send_keys("karishma yadav")
alert.accept()
