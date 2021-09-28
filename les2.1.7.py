#!/usr/bin/env python3

from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(x)
    
    answer = browser.find_element_by_id('answer')
    answer.send_keys(y)
    
    submit = browser.find_element_by_class_name('btn-default')
    submit.click()

     
finally:
    time.sleep(10)
    browser.quit()


