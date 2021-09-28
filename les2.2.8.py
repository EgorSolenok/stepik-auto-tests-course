#!/usr/bin/env python3

from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)
    #Создание нового файла в директории
    #with open("test.txt", "w") as file:
    #    content = file.write("automationbypython")  # create test.txt file
    
    browser.find_element_by_xpath("//input[@name='firstname']").send_keys("Major")
    browser.find_element_by_xpath("//input[@name='lastname']").send_keys("Major")
    browser.find_element_by_xpath("//input[@name='email']").send_keys("Major")
    
    download_file = browser.find_element_by_xpath("//input[@type='file']")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))
    file_path = os.path.join(current_dir, 'com_seleium.txt')
    download_file.send_keys(file_path)
    

    submit = browser.find_element_by_xpath("//button[@type='submit']")
    submit.click()
    
    

                                     

finally:
    time.sleep(10)
    browser.quit()


