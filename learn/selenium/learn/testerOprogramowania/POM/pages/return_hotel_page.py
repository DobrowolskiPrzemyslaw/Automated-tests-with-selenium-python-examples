from selenium.webdriver.common.by import By
class ReturnHotelPage:
    def __init__(self, driver):
        self.driver = driver
        self.hotel_names_xpath = "//h4[contains(@class,'list_title')]//b"
        self.hotel_prices_xpath = "//div[@class='fs26 text-center']//b"
    def get_names_of_hotels(self):
        hotel_names = self.driver.find_elements(By.XPATH, self.hotel_names_xpath)
        return [hotel.get_attribute("textContent") for hotel in hotel_names]
    def get_prices_of_hotels(self):
        hotel_prices = self.driver.find_elements(By.XPATH, self.hotel_prices_xpath)
        return [hotel.get_attribute("textContent") for hotel in hotel_prices]