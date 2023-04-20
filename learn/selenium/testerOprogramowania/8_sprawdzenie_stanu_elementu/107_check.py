from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
element = driver.find_element(By.NAME, "fname")

if element.is_selected():
    print("Element jest zaznaczony")
else:
    print("Element nie jest zaznaczony")
input('Press enter to continue...')