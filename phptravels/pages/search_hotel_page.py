import logging
import allure
from allure_commons.types import AttachmentType

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
    @allure.step("Setting city name to '{1}'")
    def set_city_name(self,city_name):
        self.logger.info("Setting city")
        self.driver.find_element(By.XPATH, self.search_hotel_span_xpath).click()
        self.driver.find_element(By.XPATH, self.search_hotel_input_xpath).send_keys(city_name)
        self.driver.find_element(By.XPATH, self.location_match_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)

    @allure.step("Setting dates checkin '{1}' and chechout '{2}'")
    def set_date(self, checkin, checkout):
        self.logger.info("Setting checkin date {} and checkout date {}".format(checkin,checkout))
        self.driver.find_element(By.NAME, self.checkin_name).send_keys(checkin)
        self.driver.find_element(By.NAME, self.checkout_name).send_keys(checkout)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_date", attachment_type=AttachmentType.PNG)

    @allure.step("Setting number travelers: adults '{1}' and children '{2}'")
    def set_number_travelers(self, number_of_adults,number_of_children):
        self.logger.info("Setting number of adults: {} and number of child {}".format(number_of_adults, number_of_children))
        self.driver.find_element(By.ID, self.travellers_input_id).click()
        self.driver.find_element(By.ID, self.adult_input_id).clear()
        self.driver.find_element(By.ID, self.adult_input_id).send_keys(number_of_adults)
        self.driver.find_element(By.ID, self.child_input_id).clear()
        self.driver.find_element(By.ID, self.child_input_id).send_keys(number_of_children)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travelers", attachment_type=AttachmentType.PNG)
    def click_search_button(self):
        self.logger.info("Performing search button")
        self.driver.find_element(By.XPATH, self.search_button_xpath).click()