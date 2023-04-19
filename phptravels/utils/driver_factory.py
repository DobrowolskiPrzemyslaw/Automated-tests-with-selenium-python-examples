from selenium import webdriver

class DriverFactory:

    def get_driver(browser):
        if browser == "chrome":
            return webdriver.Chrome()
        elif browser == "firefox":
            return webdriver.Firefox()
        raise Exception("Provide valid driver name")