from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
element = driver.find_element(By.NAME, "fname")
if element.is_enabled():
    element.send_keys("Element jest dostępny")
else:
    print("Element nie jest dostępny")
input('Press enter to continue...')