# Работа с помощью Selenium.
# Провести тест, с записью результатов.
# Можно написать тест любого сайта, на котором есть регистрация и radio button,
# checkbox
# Критерии: вход на сайт, запись полученных результатов, запись выбранных вариантов,
# проверка на все возможные варианты ответа.
# Варианты сайтов: .
# https://replit.com/
# https://myshows.me/


# Open https://dominos.ua/uk/kyiv/' - Pass
# Go to site header - Pass
# Click on "Увійти" button - Pass
# Click on "Реєстрація" button - Pass
# Open window.open('https://mail.tm/ru/') - Pass
# Copy temp mail e-mail on the site header by clicking on it - Pass
# Go back to "Реєстрація" section of the dominos.ua - Pass
# Fill e-mail line - Pass
# Fill Password line - Pass
# Re-enter password - Pass
# Click on the "Реєстрація" button - Pass
# Go back to the temp mail - Pass
# Click on the received e-mail - Pass
# Click on "Підтвердити" link - Fail
# Go back to the dominos.ua - Pass
# Click on the "Увійти" button - Pass
# Fill the e-mail line - Pass
# Fill Password line - Pass
# Click on the "Увійти" button - Fail


# Description: Possibility of logining in the Dominos site
# Expected result - Correct login in after entering the correct e-mail and password and clicking the "Увійти" button
# Actual result - After clicking "Увійти" button redirecting to white screen instead of correct login in
# Steps to reproduce:
# Open https://dominos.ua/uk/kyiv/' - Pass
# Go to site header - Pass
# Click on "Увійти" button - Pass
# Click on "Реєстрація" button - Pass
# Fill e-mail line - Pass
# Fill Password line - Pass
# Click on "Увійти" button - Fail
# Priority: Critical
# Severity: Blocker








from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from XPATH import main_page
import time




driver = webdriver.Chrome()
driver.get('https://dominos.ua/uk/kyiv/')
driver.execute_script("window.open('https://mail.tm/ru/')")
driver.maximize_window()
driver.switch_to.window((driver.window_handles[-1]))
time.sleep(5)
driver.switch_to.window(driver.window_handles[0])
time.sleep(5)



enter_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.enter_button)
    )
)

enter_button.click()

reg_button1 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.reg_button1)
    )
)
reg_button1.click()

driver.switch_to.window((driver.window_handles[-1]))
time.sleep(5)

temp_mail = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.temp_mail)
    )
)
temp_mail.click()
driver.switch_to.window((driver.window_handles[0]))
time.sleep(5)

reg_line_log = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.reg_line_log)
    )
)
reg_line_log.click()
reg_line_log.send_keys(Keys.CONTROL + "v")



reg_line_pass1 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.reg_line_pass1)
    )
)
reg_line_pass1.click()
reg_line_pass1.send_keys("asdasd12")



reg_line_pass2 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.reg_line_pass2)
    )
)
reg_line_pass2.click()
reg_line_pass2.send_keys("asdasd12")


reg_button2 = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.reg_button2)
    )
)
reg_button2.click()

driver.switch_to.window((driver.window_handles[-1]))
time.sleep(5)

open_mail = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.open_mail)
    )
)
open_mail.click()
time.sleep(5)



driver.switch_to.window((driver.window_handles[0]))
time.sleep(5)


close_popup_wind = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.close_popup_wind)
    )
)
close_popup_wind.click()


enter_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, main_page.enter_button)
        )
    )
enter_button.click()

log_line = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.log_line)
    )
)
log_line.click()
log_line.send_keys("viktorkovalyovvv@gmail.com")

pass_line = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.pass_line)
    )
)
pass_line.click()
pass_line.send_keys("qwerty123")

enter_button2 = WebDriverWait(driver, 60). until(
    EC.element_to_be_clickable(
        (By.XPATH,main_page.enter_button2)
    )
)
enter_button2.click()






