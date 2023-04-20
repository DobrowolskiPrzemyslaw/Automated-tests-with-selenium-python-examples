import logging
import allure
from allure_commons.types import AttachmentType

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class SearchFlightPage:

    def __init__(self, driver):
        self.driver = driver
        self.flight_page_button_xpath = "//span[text()='Flights  ']"
        self.city_span_xpath = "//span[text()='Enter City Or Airport']"
        self.active_city_input_xpath = "//div[@id='select2-drop']//input"
        self.airport_match_input_xpath = "//ul[@class='select2-results']//span"

        self.departure_date_input_xpath = "//input[@placeholder='Depart']"
        self.return_date_input_xpath = "//input[@placeholder='Return']"
        self.round_trip_checkbox_xpath = "//div[@class='iradio_square-grey']//ins"

        self.number_of_travelers_input_name = "totalManualPassenger"
        self.adults_select_xpath = "//select[@name='madult']"
        self.children_select_xpath = "//select[@name='mchildren']"
        self.infant_select_xpath = "//select[@name='minfant']"
        self.submit_button_xpath = "//button[@id='sumManualPassenger']"
        self.search_button_xpath = "//button[@class='btn-primary btn btn-lg btn-block pfb0']"
        logging.basicConfig(filename='selenium.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)
    @allure.step("Setting start city '{1}' and target city '{2}'")
    def set_airports(self,start_city_name, target_city_name):
        self.logger.info(f"Setting start city {start_city_name} and target city {target_city_name}")
        self.driver.find_element(By.XPATH, self.flight_page_button_xpath).click()
        self.driver.find_element(By.XPATH, self.round_trip_checkbox_xpath).click()
        self.driver.find_element(By.XPATH, self.city_span_xpath).click()
        self.driver.find_element(By.XPATH, self.active_city_input_xpath).send_keys(start_city_name)
        self.driver.find_element(By.XPATH, self.airport_match_input_xpath).click()

        self.driver.find_element(By.XPATH, self.city_span_xpath).click()
        self.driver.find_element(By.XPATH, self.active_city_input_xpath).send_keys(target_city_name)
        self.driver.find_element(By.XPATH, self.airport_match_input_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_cities", attachment_type=AttachmentType.PNG)

    @allure.step("Setting departure date '{1}' and return date '{2}'")
    def set_dates(self, departure_date, return_date):
        self.logger.info(f"Setting departure date {departure_date} and return date {return_date}")
        self.driver.find_element(By.XPATH, self.departure_date_input_xpath).send_keys(departure_date)
        self.driver.find_element(By.XPATH, self.return_date_input_xpath).send_keys(return_date)
        allure.attach(self.driver.get_screenshot_as_png(), name="set_dates", attachment_type=AttachmentType.PNG)

    @allure.step("Setting number of travelers'")
    def set_travelers(self):
        self.logger.info("Setting number of travelers")
        self.driver.find_element(By.NAME, self.number_of_travelers_input_name).click()
        WebDriverWait(self.driver, timeout=5).until(lambda d: d.find_element(By.XPATH, self.adults_select_xpath).is_displayed())
        select = Select(self.driver.find_element(By.XPATH, self.adults_select_xpath))
        select.select_by_index(1)
        select = Select(self.driver.find_element(By.XPATH, self.children_select_xpath))
        select.select_by_index(1)
        select = Select(self.driver.find_element(By.XPATH, self.infant_select_xpath))
        select.select_by_index(1)
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
        allure.attach(self.driver.get_screenshot_as_png(), name="set_travelers", attachment_type=AttachmentType.PNG)

    @allure.step("Clicking search button'")
    def search_flights(self):
        self.driver.find_element(By.XPATH,  self.search_button_xpath).click()
