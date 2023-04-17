from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://demos.telerik.com/kendo-ui/dragdrop/index")
driver.maximize_window()
driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
draggable = driver.find_element(By.XPATH, "//div[@id='draggable']")
droptarget = driver.find_element(By.XPATH, "//div[@id='droptarget']")
actions = ActionChains(driver)
actions.drag_and_drop(draggable,droptarget).perform()
input('Press enter to continue...')