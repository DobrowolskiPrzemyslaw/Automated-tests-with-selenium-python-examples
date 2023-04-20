from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
driver.maximize_window()
click_me_button = driver.find_element(By.ID, "newPage")
click_me_button.click()
current_window_handle = driver.current_window_handle
window_names = driver.window_handles

for window in window_names:
    if window != current_window_handle:
        driver.switch_to.window(window)

print(driver.title)
driver.switch_to.window(current_window_handle)