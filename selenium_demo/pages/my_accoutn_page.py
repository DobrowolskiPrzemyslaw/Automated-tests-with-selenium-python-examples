from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from selenium_demo.locators.locators import MyAccountLocators


class MyAccoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input_id = MyAccountLocators.username_input_id
        self.password_input_id = MyAccountLocators.password_input_id
        self.reg_email_input_id = MyAccountLocators.reg_email_input_id
        self.reg_password_input_id = MyAccountLocators.reg_password_input_id
        self.my_account_xpath = MyAccountLocators.my_account_xpath
        self.error_msg_xpath = MyAccountLocators.error_msg_xpath
        self.logout_link = MyAccountLocators.logout_link

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input_id).send_keys(username)
        self.driver.find_element(*self.password_input_id).send_keys(password)
        self.driver.find_element(*self.password_input_id).send_keys(Keys.ENTER)

    def create_account(self, email, password):
        self.driver.find_element(*self.reg_email_input_id).send_keys(email)
        self.driver.find_element(*self.reg_password_input_id).send_keys(password)
        self.driver.find_element(*self.reg_password_input_id).send_keys(Keys.ENTER)

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg_xpath).text