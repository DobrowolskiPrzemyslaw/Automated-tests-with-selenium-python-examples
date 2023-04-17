from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
autoSelect =  Select(driver.find_element(By.TAG_NAME, "select"))
autoSelect.select_by_visible_text("Volvo")
autoSelect.select_by_value("saab")
autoSelect.select_by_index(0)
input('Press enter to continue...')