from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #link1="http://suninjuly.github.io/math.html"
    link2 = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    #browser.get(link1)
    browser.get(link2)

    # код, который заполняет обязательные поля
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    print(x)
    y = calc(x)

    input1= browser.find_element_by_id("answer")
    input1.send_keys(y)

    checkbox1= browser.find_element_by_id("robotCheckbox")
    checkbox1.click()

    radiobutton1=browser.find_element_by_id("robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView({block: 'center'});", radiobutton1)
    radiobutton1.click()


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





