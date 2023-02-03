from selenium.common import NoSuchElementException
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def is_basket_is_empty(self):
		try:
			self.browser.find_element(*BasketPageLocators.ORDER_TOTAL)
		except NoSuchElementException:
			return True

		return False

	def is_basket_is_empty_message(self):
		try:
			self.browser.find_element(*BasketPageLocators.EMPTY_BASKET)
		except NoSuchElementException:
			return False

		return True
