from selenium import webdriver
from pages.login_page import LoginPage
import time

def test_valid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    time.sleep(2)
    assert "inventory" in driver.current_url

    driver.quit()


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")

    login_page = LoginPage(driver)
    login_page.login("invalid_user", "wrong_password")

    time.sleep(2)
    error = login_page.get_error_message()

    assert "Username and password do not match" in error

    driver.quit()