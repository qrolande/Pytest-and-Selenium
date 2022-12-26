import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение и считаем его по формуле
    x_element = browser.find_element(By.CSS_SELECTOR, "[id=input_value]")
    x = x_element.text
    y = calc(x)

    # Находим строку ввода и вставляем туда полученное значение
    input1 = browser.find_element(By.CSS_SELECTOR, "[id=answer]")
    input1.send_keys(y)

    # Находим необхдимый чекбокс и выбираем его
    checkbox = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    checkbox.click()

    # Находим нужный радиобатон и выбираем его
    radiob = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    radiob.click()

    # Кликаем на submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
