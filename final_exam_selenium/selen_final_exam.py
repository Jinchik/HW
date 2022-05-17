# Работа с помощью Selenium.
# Провести тест, с записью результатов.
# Можно написать тест любого сайта, на котором есть регистрация и radio button,
# checkbox
# Критерии: вход на сайт, запись полученных результатов, запись выбранных вариантов,
# проверка на все возможные варианты ответа.
# Варианты сайтов: .
# https://replit.com/
# https://myshows.me/


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
time.sleep(10)

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
time.sleep(10)

open_mail = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.open_mail)
    )
)
open_mail.click()

mail_accept = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, main_page.mail_accept)
    )
)
mail_accept.click()

driver.close()


# enter_button = WebDriverWait(driver, 60).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, main_page.enter_button)
#     )
# )
# enter_button.click()

#
# user_sign_up = WebDriverWait(driver, 60).until(
#     EC.element_to_be_clickable(
#         (By.XPATH, main_page.user_sign_up)
#     )
# )
# user_sign_up.click()
# user_sign_up.send_keys("asdasd")
# user_sign_up.send_keys("12312312")
