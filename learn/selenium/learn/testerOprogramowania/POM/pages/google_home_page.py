from selenium.webdriver.common.by import By
class GoogleHomePage:
    def __init(self, driver):
        self.driver = driver
        self.search_input_name = 'q'
        self.search_button_name = 'btnK'
        self.accept_button_xpath = "//*[@id=\"L2AGLb\"]"

    def close_popup(self):
        self.driver.switch_to.frame(1)
        self.driver.find_element(By.ID, self.accept_button_xpath).click()
    def search_in_google(self,text):
        self.driver.switch_to.default_content()
        self.driver.find_element(By.NAME, self.search_input_name).send_keys(text)
        self.driver.find_element(By.NAME, self.search_input_name).click()