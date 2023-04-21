from selenium.webdriver.common.by import By


class BillingAddressLocators:
    reg_email_id = (By.ID, "reg_email")
    reg_password_id = (By.ID, "reg_password")
    addresses_link = (By.LINK_TEXT, "Addresses")
    edit_link = (By.LINK_TEXT, "Edit")
    billing_first_name_id = (By.ID, "billing_first_name")
    billing_last_name_id = (By.ID, "billing_last_name")
    billing_country_id = (By.ID, "billing_country")
    billing_address_id = (By.ID, "billing_address_1")
    billing_postcode_id = (By.ID, "billing_postcode")
    billing_city_id = (By.ID, "billing_city")
    billing_phone_id = (By.ID, "billing_phone")
    save_address_button_xpath = (By.XPATH, "//button[text()='Save address']")
    success_msg_xpath = (By.XPATH, "//*[@class='woocommerce-message']")

class MyAccountLocators:
    username_input_id = (By.ID, "username")
    password_input_id = (By.ID, "password")
    reg_email_input_id = (By.ID, "reg_email")
    reg_password_input_id = (By.ID, "reg_password")
    my_account_xpath = (By.XPATH, "//li[@id='menu-item-22']//a")
    error_msg_xpath = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    logout_link = (By.LINK_TEXT, "Logout")