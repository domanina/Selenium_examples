import unittest
from selenium import webdriver
import time


class MyTestCase(unittest.TestCase):
    def test_1_link_no_errors(self):

        link2 = "http://suninjuly.github.io/registration1.html"
        #link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()

        # browser.get(link)
        browser.get(link2)
        elements = browser.find_elements_by_tag_name("input[required]")

        self.assertEqual(3, len(elements), "Must be 3 elements")

        for element in elements:
            element.send_keys("Мой ответ")
            time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text


        self.assertEqual(welcome_text,"Congratulations! You have successfully registered!","Registration was not passed")

    def test_2_link_errors(self):

        #link2 = "http://suninjuly.github.io/registration1.html"
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()

        # browser.get(link)
        browser.get(link2)
        elements = browser.find_elements_by_tag_name("input[required]")

        self.assertEqual(3, len(elements), "Must be 3 elements")

        for element in elements:
            element.send_keys("Мой ответ")
            time.sleep(1)

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         "Registration was not passed")


if __name__ == '__main__':
    unittest.main()
