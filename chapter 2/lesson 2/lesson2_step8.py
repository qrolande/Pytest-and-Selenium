from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

curr_dir = current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим строку ввода и вставляем туда полученное значение
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Lol")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Kek")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("Cheburek")

    # Находим кнопку загрузки файла и кликаем на нее
    file_button = browser.find_element(By.ID, "file")
    file_button.send_keys(file_path)

    # Кликаем на submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()
    time.sleep(5)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
