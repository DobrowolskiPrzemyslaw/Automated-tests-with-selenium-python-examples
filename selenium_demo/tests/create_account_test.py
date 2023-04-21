import random
import pytest
from selenium.webdriver.common.by import By
from selenium_demo.pages.my_accoutn_page import MyAccoutPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    def test_create_account_failed(self):
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.create_account("wp@wp.pl", "password")
        msg = "Error: An account is already registered with your email address."
        assert msg in my_accout_page.get_error_msg()

    def test_create_account_passed(self):
        random_int = random.randint(0, 10000)
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.create_account(str(random_int) + "wp@wp.pl", "password")
        assert self.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
