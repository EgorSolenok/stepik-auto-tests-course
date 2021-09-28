#!/usr/bin/env python3

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    browser = webdriver.Chrome()
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    time.sleep(3)
    browser.quit()


