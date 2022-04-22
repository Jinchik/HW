from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import footer_menu_xpath

# 3 - Check footer menu
# Check list:
# Open http://yanigen.com.ua (pass)
# Click on ru language button on right corner of header (pass)
# Click on ГЛАВНАЯ button on the site footer menu (pass)
# Click on ИЗДЕЛИЯ НА ЗАКАЗ button on the site footer menu (pass)
# Click on КАТАЛОГ button on the site footer menu (pass)
# Click on КЛИЕНТАМ button on the site footer menu (pass)
# Click on О НАС button on the site footer menu (pass)
# Click on КОНТАКТЫ button on the site footer menu (pass)

driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua')
driver.maximize_window()

ru_lang = '//li[@class="lang-active"]/a[@href="/ru/"]'
ru_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, ru_lang)
    )
)
ru_lang_button.click()


main_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.main_ru)
    )
)
main_ru_button.click()


productstoorder_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.productstoorder_ru)
    )
)
productstoorder_ru_button.click()


categories_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.categories_ru)
    )
)
categories_ru_button.click()


toclients_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.toclients_ru)
    )
)
toclients_ru_button.click()


aboutus_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.aboutus_ru)
    )
)
aboutus_ru_button.click()


contacts_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, footer_menu_xpath.contacts_ru)
    )
)
contacts_ru_button.click()
