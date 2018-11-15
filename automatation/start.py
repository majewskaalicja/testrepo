import os

from selenium import webdriver


chrome_driver_path = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("https://www.facebook.com/")
email_input = driver.find_element_by_css_selector("#email")
password_input = driver.find_element_by_css_selector("#pass")
# some_text = elem.text
email_input.send_keys("alicja.cechel@gmail.com")
password_input.send_keys("aalicjaa241993r..")

# print(some_text)
driver.find_element_by_css_selector('[data-testid=royal_login_button]').click()

driver.close()