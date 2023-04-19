from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("http://www.kurs-selenium.pl/demo/")
driver.maximize_window()
driver.find_element(By.XPATH,"//span[text()='Search by Hotel or City Name']").click()
driver.find_element(By.XPATH,"//div[@id='select2-drop']//input").send_keys("Dubai")
driver.find_element(By.XPATH,"//span[text()='Dubai']").click()
driver.find_element(By.NAME,"checkin").send_keys("12/09/2020")
driver.find_element(By.NAME,"checkout").send_keys("15/09/2020")
driver.find_element(By.ID,"travellersInput").click()
driver.find_element(By.ID,"adultInput").clear()
driver.find_element(By.ID,"adultInput").send_keys("4")
driver.find_element(By.ID,"childInput").clear()
driver.find_element(By.ID,"childInput").send_keys("1")
driver.find_element(By.XPATH,"//button[text()=' Search']").click()
hotels = driver.find_elements(By.XPATH,"//h4[contains(@class,'list_title')]//b")
hotel_names = [hotel.get_attribute("textContent") for hotel in hotels]
assert hotel_names[0] == "Jumeirah Beach Hotel"
assert hotel_names[1] == "Oasis Beach Tower"
assert hotel_names[2] == "Rose Rayhaan Rotana"
assert hotel_names[3] == "Hyatt Regency Perth"
hotels_prices = driver.find_elements(By.XPATH, "//div[@class='fs26 text-center']//b") # lista webElementow
hotel_prices = [hotel.get_attribute("textContent") for hotel in hotels_prices]        # lista nazw .get_attribute("textContent") mozna wykonac na pojedynczym elemencie
assert hotel_prices[0] == "€20.24"
assert hotel_prices[1] == "€46"
assert hotel_prices[2] == "€73.60"
assert hotel_prices[3] == "€138"
