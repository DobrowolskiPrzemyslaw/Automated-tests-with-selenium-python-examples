from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Waits.html")
driver.maximize_window()
WebDriverWait(driver, timeout=10).until(expected_conditions.visibility_of(driver.find_element(By.ID, "clickOnMe")))
WebDriverWait(driver, timeout=3).until(lambda d: d.find_element(By.TAG_NAME,"p"))
driver.find_element(By.ID, "clickOnMe").click()
print(driver.find_element(By.TAG_NAME,"p").text)
# input('Press enter to continue...')