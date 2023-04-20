from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Waits.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
print(driver.find_element(By.TAG_NAME,"p").text)
# input('Press enter to continue...')