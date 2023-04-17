from selenium import webdriver
from selenium.webdriver.common.by import By

# https://www.selenium.dev/documentation/webdriver/elements/finders/

driver = webdriver.Chrome()
driver.get("https://www.example.com")

vegetable = driver.find_element(By.CLASS_NAME, "tomatoes")
fruits = driver.find_element(By.ID, "fruits")
fruit = fruits.find_element(By.CLASS_NAME, "tomatoes")
plants = driver.find_elements(By.TAG_NAME, "li")
elements = driver.find_elements(By.TAG_NAME, 'p')

fruit = driver.find_element(By.CSS_SELECTOR, "#fruits .tomatoes")
fruita = driver.find_element(By.XPATH, "//a")

for e in elements:
    print(e.text)
