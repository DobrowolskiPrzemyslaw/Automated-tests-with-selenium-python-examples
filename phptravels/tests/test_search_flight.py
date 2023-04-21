import allure
import pytest

from phptravels.pages.result_flights_page import ResultFlightPage
from phptravels.pages.search_flights_page import SearchFlightPage

@pytest.mark.usefixtures("setup")
class TestSearchHotel:

    @allure.title("Flight Page Test")
    @allure.feature("Search flights feature")
    @allure.story("Story")
    @allure.description("Search flight from Dubai to Warsaw")
    def test_names_hotels(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_flights = SearchFlightPage(self.driver)
        search_flights.set_airports("Dubai", "Warsaw")
        search_flights.set_dates("12/09/2020", "15/09/2020")
        search_flights.set_travelers()
        search_flights.search_flights()
        result_flights = ResultFlightPage(self.driver)
        text = result_flights.get_result_text()
        assert text == "No Results Found"