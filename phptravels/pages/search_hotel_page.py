import logging

from selenium.webdriver.common.by import By
class SearchHotelPage:

    def __init__(self, driver):
        self.driver = driver
        self.search_hotel_span_xpath = "//span[text()='Search by Hotel or City Name']"
        self.search_hotel_input_xpath = "//div[@id='select2-drop']//input"
        self.location_match_xpath = "//span[text()='Dubai']"
        self.checkin_name = "checkin"
        self.checkout_name = "checkout"
        self.travellers_input_id = "travellersInput"
        self.adult_input_id = "adultInput"
        self.child_input_id = "childInput"
        self.search_button_xpath = "//button[text()=' Search']"
        logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)
    def set_city_name(self,city_name):
        self.logger.info("Setting city")
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city_name)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()
    def set_date(self, checkin, checkout):
        logging.info("Setting checkin date {} and checkout date {}".format(checkin,checkout))
        self.driver.find_element(By.NAME, self.checkin_name).send_keys(checkin)
        self.driver.find_element(By.NAME, self.checkout_name).send_keys(checkout)
    def set_number_travelers(self, number_of_adults,number_of_child):
        logging.info("Setting number of adults: {} and number of child {}".format(number_of_adults, number_of_child))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(number_of_adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(number_of_child)
    def click_search_button(self):
        logging.info("Performing search button")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()