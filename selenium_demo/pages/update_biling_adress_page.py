from selenium.webdriver.support.select import Select

from selenium_demo.locators.locators import BillingAddressLocators


class UpDateBilingAdressPage:
    def __init__(self,driver):
        self.driver = driver
        self.reg_email_id = BillingAddressLocators.reg_email_id
        self.reg_password_id = BillingAddressLocators.reg_password_id
        self.addresses_link = BillingAddressLocators.addresses_link
        self.edit_link = BillingAddressLocators.edit_link
        self.billing_first_name_id = BillingAddressLocators.billing_first_name_id
        self.billing_last_name_id = BillingAddressLocators.billing_last_name_id
        self.billing_country_id = BillingAddressLocators.billing_country_id
        self.billing_address_id = BillingAddressLocators.billing_address_id
        self.billing_postcode_id = BillingAddressLocators.billing_postcode_id
        self.billing_city_id = BillingAddressLocators.billing_city_id
        self.billing_phone_id = BillingAddressLocators.billing_phone_id
        self.save_address_button_xpath = BillingAddressLocators.save_address_button_xpath
        self.success_msg_xpath = BillingAddressLocators.success_msg_xpath

    def open_edit_biling_address(self):
        self.driver.find_element(*self.addresses_link).click()
        self.driver.find_element(*self.edit_link).click()

    def set_personal_data(self, firs_name, last_name):
        self.driver.find_element(*self.billing_first_name_id).send_keys(firs_name)
        self.driver.find_element(*self.billing_last_name_id).send_keys(last_name)

    def select_country(self, country):
        Select(self.driver.find_element(*self.billing_country_id)).select_by_visible_text(country)

    def set_adress(self, street, post_code, city):
        self.driver.find_element(*self.billing_address_id).send_keys(street)
        self.driver.find_element(*self.billing_postcode_id).send_keys(post_code)
        self.driver.find_element(*self.billing_city_id).send_keys(city)

    def set_phone_number(self, number):
        self.driver.find_element(*self.billing_phone_id).send_keys(number)

    def save_address(self):
        self.driver.find_element(*self.save_address_button_xpath).click()

    def get_message(self):
        return self.driver.find_element(*self.success_msg_xpath).text