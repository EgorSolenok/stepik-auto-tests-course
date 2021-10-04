#!/usr/bin/env python3

import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="class")
def launch_browser():
    print("\nStart browser for test")
    launch_browser = webdriver.Chrome()
    yield launch_browser
    print("\nQuit browser..")
    launch_browser.quit()




class TestAlienAnswer():

    full = ""
    
    link_list = [
    ("link_1", "https://stepik.org/lesson/236895/step/1"),
    ("link_2", "https://stepik.org/lesson/236896/step/1"),
    ("link_3", "https://stepik.org/lesson/236897/step/1"),
    ("link_4", "https://stepik.org/lesson/236898/step/1"),
    ("link_5", "https://stepik.org/lesson/236899/step/1"),
    ("link_6", "https://stepik.org/lesson/236903/step/1"),
    ("link_7", "https://stepik.org/lesson/236904/step/1"),
    ("link_8", "https://stepik.org/lesson/236905/step/1"),
]

    @pytest.mark.parametrize("link_number, link_url", link_list)
    def test_guest_should_put_answer(self, launch_browser, link_number, link_url):

        answer = str(math.log(int(time.time()) + 0.23))
        
        launch_browser.get(f"{link_url}")
        print(f"\nCheking {link_number}, {link_url}")
        text_area = WebDriverWait( launch_browser, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//textarea"))
        )
        text_area.send_keys(str(answer))
        
        WebDriverWait(launch_browser, 8).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']"))
        ).click()
        alien_answer = WebDriverWait(launch_browser, 8).until(
            EC.visibility_of_element_located((By.XPATH, "//pre"))
        ).text
        
        if alien_answer != "Correct!":
            self.full += alien_answer
        print(self.full)

if __name__ == "__main__":
    unittest.main()
