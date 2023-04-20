import random

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_create_account_failed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    driver.find_element(By.ID, "reg_email").send_keys("eamil@wp.pl")
    driver.find_element(By.ID, "reg_password").send_keys("password")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    msg = "Error: An account is already registered with your email address."
    assert msg in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text
    driver.quit()

def test_create_account_passed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com/?page_id=7")
    random_int = random.randint(0, 10000)
    driver.find_element(By.ID, "reg_email").send_keys(f"eamil{random_int}@wp.pl")
    driver.find_element(By.ID, "reg_password").send_keys("password")
    driver.find_element(By.ID, "reg_password").send_keys(Keys.ENTER)
    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    driver.quit()