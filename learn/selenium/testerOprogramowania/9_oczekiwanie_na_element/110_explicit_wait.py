from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Waits.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
wait = WebDriverWait(driver, timeout=10)
element = wait.until(expected_conditions.visibility_of_element_located((By.TAG_NAME,"p")))
print(element.text)
# input('Press enter to continue...')