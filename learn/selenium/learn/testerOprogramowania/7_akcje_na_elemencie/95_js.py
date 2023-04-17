from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
wartosc = "Wpisz cos"
driver.execute_script("arguments[0].setAttribute('value','" + wartosc + "');",driver.find_element(By.ID, "fname"))
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "newPage"))
input('Press enter to continue...')

