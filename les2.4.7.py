#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100")
    )
    browser.find_element_by_xpath("//button[@id='book']").click()

    x = browser.find_element_by_xpath("//span[@id='input_value']").text
    y = calc(x)
    
    browser.find_element_by_id('answer').send_keys(y)

    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    time.sleep(10)
    browser.quit()
    