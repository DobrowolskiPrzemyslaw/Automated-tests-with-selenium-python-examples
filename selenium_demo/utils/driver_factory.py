from selenium import webdriver


class DriverFactory:
    def get_driver(self):
        if self == "chrome":
            return webdriver.Chrome()
        elif self == "firefox":
            return webdriver.Firefox()
        raise Exception("Provide valid driver name")
