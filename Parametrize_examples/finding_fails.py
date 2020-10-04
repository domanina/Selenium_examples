from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.fixture (scope = "function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()



@pytest.mark.parametrize('links', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"])
def test_link(browser, links):
    link = links

    answer = math.log(int(time.time()))
    print(answer)
    text_answer = str(answer)
    #browser = webdriver.Chrome()
    browser.get(link)


    input1=WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "textarea.string-quiz__textarea.ember-text-area.ember-view"))
    )
    input1.send_keys(text_answer)

    button2 = browser.find_element_by_class_name("submit-submission")
    button2.click()


    text_result = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    )

    actual_result = text_result.text
    expected_result = "Correct!"


    assert expected_result==actual_result, f"Expected {expected_result}, got {actual_result} "




