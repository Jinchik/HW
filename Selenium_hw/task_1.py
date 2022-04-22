from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1 - Open site
# Check list:
# Open http://yanigen.com.ua (pass)


driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua')
driver.maximize_window()


