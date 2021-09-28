#!/usr/bin/env python3

from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_first_element = browser.find_element_by_xpath("//span[@id='num1']")
    x_second_element = browser.find_element_by_xpath("//span[@id='num2']")
    y_element = str(int(x_first_element.text) + int(x_second_element.text))
    answer = Select(browser.find_element_by_xpath("//select"))
    answer.select_by_value(str(y_element))


    submit = browser.find_element_by_class_name('btn-default')
    submit.click()

finally:
    time.sleep(15)
    browser.quit()


