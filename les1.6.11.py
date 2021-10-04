#!/usr/bin/env python3

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_css_selector('.first_block [required].first')
    input1.send_keys('One')
    input2 = browser.find_element_by_css_selector('.first_block [required].second')
    input2.send_keys('One')
    input3 = browser.find_element_by_css_selector('.first_block [required].third')
    input3.send_keys('One')
        
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(2)
    
    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text
            
finally:
    time.sleep(10)
    browser.quit()
