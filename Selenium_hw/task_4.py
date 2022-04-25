from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import lang_buttons_xpath
# 4 - Check language menu
# Check list:
# Open http://yanigen.com.ua. Site exist was opened (pass)
# Click on ru language button on right corner of header. Button "ru" language was clickable and was clicked (pass)
# Click on en language button on right corner of header. Button "en" language was clickable and was clicked (pass)
# Click on ua language button on right corner of header. Button "ua" language was clickable and was clicked (pass)


driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua')
driver.maximize_window()


ru_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, lang_buttons_xpath.ru_lang)
    )
)
ru_lang_button.click()

eng_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, lang_buttons_xpath.eng_lang)
    )
)
eng_lang_button.click()

ua_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, lang_buttons_xpath.ua_lang)
    )
)
ua_lang_button.click()