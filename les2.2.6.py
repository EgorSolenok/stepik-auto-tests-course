#!/usr/bin/env python3

from selenium import webdriver
import time
import math

def calc(x):
    
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    link = "http://SunInJuly.github.io/execute_script.html"
    browser.get(link)
    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    
    y = calc(x)
    
    answer = browser.find_element_by_xpath("//input[@id='answer']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(y)
    
    
    checkbox = browser.find_element_by_id('robotCheckbox')
    checkbox.click()
    
    button = browser.find_element_by_id('robotsRule')
    button.click()
    

    submit = browser.find_element_by_class_name('btn-primary')
    submit.click()
    
    

                                     

finally:
    time.sleep(10)
    browser.quit()


