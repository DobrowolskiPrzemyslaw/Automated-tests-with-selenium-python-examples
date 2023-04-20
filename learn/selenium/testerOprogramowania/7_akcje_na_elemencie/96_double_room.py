from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\DoubleClick.html")
driver.maximize_window()
button = driver.find_element(By.ID, "bottom")
webdriver.ActionChains(driver).double_click(button).perform()