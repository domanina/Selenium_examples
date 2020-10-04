from selenium import webdriver
import time
import os

try:

    link1="http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link1)

    # код, который заполняет обязательные поля
    elements = browser.find_elements_by_class_name("form-control")
    for element in elements:
        element.send_keys("Мой ответ")



    #attachments

    file_cv = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'cv.txt')  # добавляем к этому пути имя файла
    file_cv.send_keys(file_path)
    time.sleep(1)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()