import os

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chrome_driver_path = os.path.dirname(os.path.abspath(__file__)) + '/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver_path)


driver.get("http://www.gazeta.pl/0,0.html")
elem = driver.find_element_by_css_selector(".o-daily h2")
some_text = elem.text

print(some_text)

driver.close()