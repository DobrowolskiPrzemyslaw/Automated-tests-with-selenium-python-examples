from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\iFrameTest.html")
driver.maximize_window()
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.frame(driver.find_element(By.TAG_NAME, "iframe"))
# driver.switch_to.frame(1)
print(driver.find_element(By.TAG_NAME, "h1").text)
driver.switch_to.default_content()
print(driver.find_element(By.TAG_NAME, "h1").text)

input('Press enter to continue...')
