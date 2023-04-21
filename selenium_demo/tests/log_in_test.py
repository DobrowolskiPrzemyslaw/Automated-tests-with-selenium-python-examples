import random
import pytest
from selenium.webdriver.common.by import By
from selenium_demo.pages.my_accoutn_page import MyAccoutPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    def test_login_passed(self):
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("wp@wp.pl", "password")
        assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

    def test_login_incorrect_password(self):
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("wp@wp.pl", "password123")
        msg = "ERROR: Incorrect username or password."
        assert msg in my_accout_page.get_error_msg()
    def test_login_empty_password(self):
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("wp@wp.pl", "")
        msg = "ERROR: The password field is empty."
        assert msg in my_accout_page.get_error_msg()

    def test_login_empty_username(self):
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.log_in("", "password")
        msg = "Error: Username is required."
        assert msg in my_accout_page.get_error_msg()
