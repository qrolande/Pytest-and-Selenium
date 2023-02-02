from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL = (By.ID, "id_login-username")
    LOGIN_PASSWORD = (By.ID, "id_login-password")

    RGISTR_LOGIN = (By.ID, "id_registration-email")
    RGISTR_PASSWORD = (By.ID, "id_registration-password1")
    RGISTR_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")

class TheShellcodersHandboolLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    BOOK_NAME = (By.TAG_NAME, "h1")
    PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    IS_AVAILABLE = (By.CLASS_NAME, "icon-ok")
    ANSWER_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    ANSWER_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
