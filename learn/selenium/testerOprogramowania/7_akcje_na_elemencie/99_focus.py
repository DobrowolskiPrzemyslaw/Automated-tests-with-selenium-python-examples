from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://w3schools.com")
driver.maximize_window()
driver.find_element(By.ID, "accept-choices").click()
hover_element = driver.find_element(By.ID, "navbtn_tutorials")
actions = ActionChains(driver)
actions.move_to_element(hover_element).perform()
input('Press enter to continue...')