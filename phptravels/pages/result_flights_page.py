import logging
import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ResultFlightPage:

    def __init__(self, driver):
        self.driver = driver
        self.result_text_xpath = "//div[@class='alert alert-danger']"
        logging.basicConfig(filename='selenium.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')
        self.logger = logging.getLogger(__name__)

    @allure.step("Getting result")
    def get_result_text(self):
        self.logger.info("Getting result text")
        allure.attach(self.driver.get_screenshot_as_png(), name="result_search_flight", attachment_type=AttachmentType.PNG)
        return self.driver.find_element(By.XPATH, self.result_text_xpath).text