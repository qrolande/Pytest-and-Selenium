import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser = webdriver.Chrome()
	browser.implicitly_wait(5)
	browser.get(link)

	book = browser.find_element(By.ID, "book")
	button = WebDriverWait(browser, 12).until(
		EC.text_to_be_present_in_element((By.ID, "price"), "100")
	)

	book.click()

	x = browser.find_element(By.ID, "input_value")
	y = calc(x.text)

	input1 = browser.find_element(By.ID, "answer")
	input1.send_keys(y)

	solve = browser.find_element(By.ID, "solve")
	solve.click()

finally:
	time.sleep(10)
	browser.quit()

