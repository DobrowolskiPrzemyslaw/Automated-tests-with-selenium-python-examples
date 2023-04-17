from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
input = driver.find_element(By.NAME, "username")
input.clear()
input.send_keys("Ponury Adam")