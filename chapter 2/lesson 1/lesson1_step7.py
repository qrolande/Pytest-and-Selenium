import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение и считаем его по формуле
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    print(x)
    y = calc(x)

    # Находим строку ввода и вставляем туда полученное значение
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    # Находим необхдимый чекбокс и выбираем его
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Находим нужный радиобатон и выбираем его
    radiob = browser.find_element(By.ID, "robotsRule")
    radiob.click()
    time.sleep(1)

    # Кликаем на submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
