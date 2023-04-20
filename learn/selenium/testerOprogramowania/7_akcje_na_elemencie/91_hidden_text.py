from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME, "p").get_attribute("textContent"))
input('Press enter to continue...')