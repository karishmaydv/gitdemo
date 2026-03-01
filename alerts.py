from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v121.fed_cm import click_dialog_button
from selenium.webdriver.support import select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://demoqa.com/automation-practice-form")
driver.find_element(By.__class__,"header-text").click()
driver.switch_to.alert.accept()