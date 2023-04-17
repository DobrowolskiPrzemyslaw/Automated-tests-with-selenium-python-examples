from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
click_me_button = driver.find_element(By.ID, "newPage")
click_me_button.click()
click_me_button.click()
input('Press enter to continue...')