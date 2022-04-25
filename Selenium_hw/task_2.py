from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import main_menu_xpath

# 2 - Check main menu
# Check list:
# Open http://yanigen.com.ua. Site exist was opened (pass)
# Click on ru language button on right corner of header. Button "ru" language was clickable and was clicked (pass)
# Click on ГЛАВНАЯ button on the site header main menu. Button "ГЛАВНАЯ" was clickable and was clicked (pass)
# Click on ИЗДЕЛИЯ НА ЗАКАЗ button on the site header main menu. Button "ИЗДЕЛИЯ НА ЗАКАЗ" was clickable and was clicked (pass)
# Click on КАТАЛОГ button on the site header main menu. Button "КАТАЛОГ" was clickable and was clicked (pass)
# Click on КЛИЕНТАМ button on the site header main menu. Button "КЛИЕНТАМ" was clickable and was clicked (pass)
# Click on О НАС button on the site header main menu. Button "О НАС" was clickable and was clicked (pass)
# Click on КОНТАКТЫ button on the site header main menu. Button "КОНТАКТЫ" was clickable and was clicked (pass)


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


home_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.home_ru)
    )
)
home_ru_button.click()


product_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.product_ru)
    )
)
product_ru_button.click()


catalog_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.catalog_ru)
    )
)
catalog_ru_button.click()


clients_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.clients_ru)
    )
)
clients_ru_button.click()


aboutus_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.aboutus_ru)
    )
)
aboutus_ru_button.click()


contacts_ru_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_menu_xpath.contacts_ru)
    )
)
contacts_ru_button.click()
