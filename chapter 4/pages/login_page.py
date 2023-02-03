from selenium.common import NoSuchElementException

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "Wrong URL"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Log in: Username area is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Log in: Password area is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.RGISTR_LOGIN), "Registration: Username area is not presented"
        assert self.is_element_present(
            *LoginPageLocators.RGISTR_PASSWORD), "Registration: Password area is not presented"
        assert self.is_element_present(
            *LoginPageLocators.RGISTR_CONFIRM_PASSWORD), "Registration: Password confirm area is not presented"

    def register_new_user(self, email, password):
        assert len(password) >= 9, "Password must be 9 or more symbols"
        login = self.browser.find_element(*LoginPageLocators.RGISTR_LOGIN)
        login.send_keys(email)

        pswd = self.browser.find_element(*LoginPageLocators.RGISTR_PASSWORD)
        pswd.send_keys(password)

        pswd_conf = self.browser.find_element(*LoginPageLocators.RGISTR_CONFIRM_PASSWORD)
        pswd_conf.send_keys(password)

        self.browser.find_element(*LoginPageLocators.REG_BUTT).click()

        try:
            self.browser.find_element(*LoginPageLocators.MESSAGE_TXT)
        except NoSuchElementException:
            return False
        return True
