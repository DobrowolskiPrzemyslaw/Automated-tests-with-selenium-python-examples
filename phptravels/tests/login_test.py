from selenium import webdriver
from selenium.webdriver.common.by import By

def test_log_in_passed():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("username")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID,"password"))
    driver.find_element(By.NAME, "login").click()

    assert driver.find_element(By.LINK_TEXT, "Logout").is_displayed()

def test_log_in_faild():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("http://seleniumdemo.com")
    driver.find_element(By.XPATH, "//li[@id='menu-item-22']//a").click()
    driver.find_element(By.ID, "username").send_keys("username")
    driver.find_element(By.ID, "password").send_keys("password")
    driver.execute_script("arguments[0].scrollIntoView(true);", driver.find_element(By.ID,"password"))
    driver.find_element(By.NAME, "login").click()

    assert  "ERROR: Too many failed login attempts. Please try again in " in driver.find_element(By.XPATH, "//ul[@class='woocommerce-error']//li").text