from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from XPATH import main_page
import time
import pytest



def test_2():
    driver = webdriver.Chrome()
    driver.get('https://dominos.ua/uk/kyiv/')
    driver.maximize_window()
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


    enter_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, main_page.enter_button)
        )
    )
    text_enter_button = enter_button.text
    assert text_enter_button == "Увійти"





    account_button = WebDriverWait(driver, 60).until(
        EC.element_to_be_clickable(
            (By.XPATH, main_page.account)
        )
    )
    text_account_button = account_button.text
    assert text_account_button == "Мій профіль"
