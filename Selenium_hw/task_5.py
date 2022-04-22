from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import money_button_xpath

# 5 -Check money menu
# Check list:
# Open http://yanigen.com.ua (pass)
# Click on грн. button on right corner of header (pass)
# Click on $ button on right corner of header (pass)

driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua')
driver.maximize_window()

dol_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, money_button_xpath.button_dol)
    )
)
dol_button.click()

ua_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, money_button_xpath.button_grn)
    )
)
ua_button.click()
