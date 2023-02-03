from selenium.common import TimeoutException

from .locators import TheShellcodersHandboolLocators
from .base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage(BasePage):
	def add_to_basket(self):
		assert self.is_element_present(*TheShellcodersHandboolLocators.ADD_TO_BASKET), "No button Add to basket"
		assert self.is_element_present(*TheShellcodersHandboolLocators.IS_AVAILABLE), "Book is unavailable"
		add_to_basket = self.browser.find_element(*TheShellcodersHandboolLocators.ADD_TO_BASKET)
		add_to_basket.click()

	def should_be_on_this_page(self):
		book_name = self.browser.find_element(*TheShellcodersHandboolLocators.BOOK_NAME).text
		price = self.browser.find_element(*TheShellcodersHandboolLocators.PRICE).text

		answer_name = self.browser.find_element(*TheShellcodersHandboolLocators.ANSWER_NAME).text
		answer_price = self.browser.find_element(*TheShellcodersHandboolLocators.ANSWER_PRICE).text

		assert book_name == answer_name, f"Wrong book name in basket: {answer_name}"
		assert price == answer_price, f"Wrong price in basket: {answer_price}"

	def is_not_element_present(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return True

		return False

	def is_disappeared(self, how, what, timeout=4):
		try:
			WebDriverWait(self.browser, timeout, 1, TimeoutException). \
				until_not(EC.presence_of_element_located((how, what)))
		except TimeoutException:
			return False

		return True
