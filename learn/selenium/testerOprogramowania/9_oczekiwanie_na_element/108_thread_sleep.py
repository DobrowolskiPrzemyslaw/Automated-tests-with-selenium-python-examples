import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Waits.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
time.sleep(5)
print(driver.find_element(By.TAG_NAME,"p").text)
input('Press enter to continue...')