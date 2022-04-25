from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from XPATH import lang_buttons_xpath
from XPATH import subscribe_xpath

# 5 - Check subscribe to news
# Check list:
# Open http://yanigen.com.ua. Site exist was opened (pass)
# Click on en language button on the top right corner of the site header. Button "en" language was clickable and was clicked (pass)
# Roll down to the site footer (pass)
# Look for text present "ПОДПИСЫВАЙТЕСЬ НА НОВОСТИ" above the name line. Text "ПОДПИСЫВАЙТЕСЬ НА НОВОСТИ" was present  (pass)
# Look for element present "Name" line. Element "Name" line was present   (pass)
# Look for element present "E-mail" line. Element "E-mail" line was present   (pass)
# Look for element present "Subscribe button" line. Element "Subscribe button" line was present   (pass)
# Try to enter Letters in the "Name" line. Letters were typed (pass)
# Try to enter Numbers in the "Name" line. Numbers were typed (pass)
# Try to enter Letters in the ""E-mail"" line. Letters were typed  (pass)
# Try to enter Numbers in the ""E-mail"" line. Numbers were typed (pass)
# Try to enter Symbols in the ""E-mail"" line. Symbols were typed (pass)
# Click on the "Subscribe button". Button "Subscribe button" was clickable and was clicked  (pass)

driver = webdriver.Chrome()
driver.get('http://yanigen.com.ua')
driver.maximize_window()

eng_lang_button = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, lang_buttons_xpath.eng_lang)
    )
)
eng_lang_button.click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located(
        (By.XPATH, subscribe_xpath.text_subscribe)
    )
)

login_line = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, subscribe_xpath.login_line)
    )
)
login_line.click()
login_line.send_keys("asdasd")
login_line.send_keys("12312312")



e_mail_line = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, subscribe_xpath.e_mail)
    )
)
e_mail_line.click()
e_mail_line.send_keys("asdasd")
e_mail_line.send_keys("@")
e_mail_line.send_keys("12312312")
e_mail_line.send_keys(".com")


sub_but = WebDriverWait(driver, 60).until(
    EC.element_to_be_clickable(
        (By.XPATH, subscribe_xpath.sub_but)
    )
)
sub_but.click()


