from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:

    link2= "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link2)

    button_submit = browser.find_element_by_css_selector("button.btn")
    button_submit.click()

    confirm = browser.switch_to.alert
    confirm.accept()


    # код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)


    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()

