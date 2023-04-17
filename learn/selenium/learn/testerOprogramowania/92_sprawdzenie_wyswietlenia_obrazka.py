from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
print(driver.find_element(By.ID, "smileImage").size.get("height"))
print(driver.find_element(By.ID, "smileImage").get_attribute("naturalHeight"))
input('Press enter to continue...')