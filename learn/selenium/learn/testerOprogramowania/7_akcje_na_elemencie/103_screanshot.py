import os.path

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\FileUpload.html")
driver.maximize_window()

upload_file = driver.find_element(By.ID, "myFile")
path = os.path.abspath("/learn/selenium/resources/uploadMe.txt")
upload_file.send_keys(path)
driver.save_screenshot("screenshot/screenshot.png")

input('Press enter to continue...')