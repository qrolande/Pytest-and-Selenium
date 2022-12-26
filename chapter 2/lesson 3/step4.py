import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/alert_accept.html"
	browser = webdriver.Chrome()
	browser.get(link)

	sub_button = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	sub_button.click()

	conf = browser.switch_to.alert
	conf.accept()

	val = browser.find_element(By.ID, "input_value")
	x = val.text
	y = calc(x)

	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)

	sub_button2 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
	sub_button2.click()

finally:
	time.sleep(10)
	browser.quit()

