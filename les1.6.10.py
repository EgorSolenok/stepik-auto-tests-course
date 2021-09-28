#!/usr/bin/env python3

from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля
    neces_inputs = browser.find_elements_by_xpath("//label[contains(text(),'*')]/following-sibling::input")
    for neces_input in neces_inputs:
        neces_input.send_keys("Answer")
        
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
