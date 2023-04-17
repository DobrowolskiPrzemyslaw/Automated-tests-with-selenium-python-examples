from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\DoubleClick.html")
driver.maximize_window()
button = driver.find_element(By.ID, "bottom")
actions = ActionChains(driver)
actions.context_click(button).perform()