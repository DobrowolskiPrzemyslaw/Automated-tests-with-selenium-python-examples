from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
click_me_button = driver.find_element(By.ID, "clickOnMe")
click_me_button.click()
driver.switch_to.alert.accept()
click_me_button.click()
driver.switch_to.alert.dismiss()
driver.find_element(By.ID, "fname").send_keys("Wpisz cos")
driver.find_element(By.ID, "password").send_keys("webdriver" + Keys.ENTER)
input('Press enter to continue...')