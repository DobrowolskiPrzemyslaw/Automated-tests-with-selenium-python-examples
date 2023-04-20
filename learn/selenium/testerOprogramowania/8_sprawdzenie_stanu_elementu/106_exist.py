from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
element = driver.find_elements(By.NAME, "fname11")

if len(element)<1:
    print("Element nie isnieje na stronie")
else:
    print("Element isnieje na stronie")
input('Press enter to continue...')