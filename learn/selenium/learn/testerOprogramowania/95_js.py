from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\iFrameTest.html")
driver.maximize_window()
driver.execute_script("arguments[0].click();", driver.find_element(By.ID, "newPage"))

wartosc = "Wpisz cos"

driver.execute_script("arguments[0].setAttribute('value','" + wartosc + "');",driver.find_element(By.ID, "fname"))