import time
import math

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestLoginForStepic():
	links = ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
			 "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
			 "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
			 "https://stepik.org/lesson/236904/step/1", "https://stepik.org/lesson/236905/step/1"]


	def log_pass_geter(self):
		file1 = open("logpass.txt", "r")
		line = file1.readlines()
		file1.close
		return line

	@pytest.mark.parametrize('links', links)
	def test_guest_should_see_login_link(self, browser, links):
		line = self.log_pass_geter()

		login = line[0]
		password = line[1]

		browser.get(links)
		browser.implicitly_wait(10)

		input1 = browser.find_element(By.CSS_SELECTOR, "[class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
		input1.click()

		input1 = browser.find_element(By.ID, "id_login_email")
		input1.send_keys(login)

		input2 = browser.find_element(By.ID, "id_login_password")
		input2.send_keys(password)

		log_in = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
		log_in.click()
		time.sleep(1)

		textarea = browser.find_element(By.TAG_NAME, "textarea")
		time.sleep(1)
		answer = math.log(int(time.time()))
		textarea.send_keys(answer)
		time.sleep(1)

		# browser.find_element(By.CLASS_NAME, "submit-submission").click()
		WebDriverWait(browser, 9).until(
			EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
		# time.sleep(3)

		res = WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
		# time.sleep(2)

		print("res = ", res)
		assert res == 'Correct!'
