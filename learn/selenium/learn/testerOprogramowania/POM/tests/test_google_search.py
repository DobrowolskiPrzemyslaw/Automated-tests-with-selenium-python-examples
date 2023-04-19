import pytest
from selenium import webdriver
from learn.selenium.learn.testerOprogramowania.POM.pages.google_home_page import GoogleHomePage
from learn.selenium.learn.testerOprogramowania.POM.pages.google_result_page import GoogleResultPage
class TestGoogleSearch:
    @pytest.fixture()
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        yield
        self.driver.quit()
    def test_google_search(self,setup):
        self.driver.get("http://www.google.com")
        home_page = GoogleHomePage(self.driver)
        home_page.close_popup()
        home_page.search_input_name("Selenium")
        result_page = GoogleResultPage(self.driver)
        result_page.open_first_result()
        input('Press enter to continue...')