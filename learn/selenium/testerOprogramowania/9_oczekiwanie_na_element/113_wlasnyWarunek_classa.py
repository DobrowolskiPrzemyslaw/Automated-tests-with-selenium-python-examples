from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class WaitForListSize:
    def __init__(self, locator):
        self.locator = locator
    def __call__(self, driver):
        return driver.find_elements(By.XPATH, self.locator)

driver = webdriver.Chrome()
driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Waits.html")
driver.maximize_window()
driver.find_element(By.ID, "clickOnMe").click()
wait = WebDriverWait(driver, timeout=10)
wait.until(WaitForListSize("//p"))
print(driver.find_element(By.TAG_NAME,"p").text)
# input('Press enter to continue...')


