from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Находим значение и считаем его по формуле
    x_element = browser.find_element(By.ID, "num1")
    x = int(x_element.text)
    print(x)

    y_element = browser.find_element(By.ID, "num2")
    y = int(y_element.text)
    print(y)
    sum = x + y
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))

    # Кликаем на submit
    submit = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    submit.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
