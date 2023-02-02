import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


def log_pass_geter():
    file1 = open("logpass.txt", "r")
    line = file1.readlines()
    file1.close
    return line

def test_guest_should_see_login_link(browser):
    line = log_pass_geter()

    login = line[0]
    password = line[1]
    browser.implicitly_wait(5)
    link = f"https://stepik.org/lesson/236895/step/1"
    browser.get(link)

    input1 = browser.find_element(By.ID, "ember33")
    input1.click()

    input1 = browser.find_element(By.ID, "id_login_email")
    input1.send_keys(login)

    input2 = browser.find_element(By.ID, "id_login_password")
    input2.send_keys(password)

    log_in = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    log_in.click()
    time.sleep(5)
