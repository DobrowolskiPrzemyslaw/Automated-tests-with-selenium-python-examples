import allure
import pytest
from pom.pages.search_hotel_page import SearchHotelPage
from pom.pages.return_hotel_page import ReturnHotelPage

@pytest.mark.usefixtures("setup")
class TestSearchHotel:

    @allure.title("Start test")
    @allure.feature("Feature")
    @allure.story("Story")
    @allure.description("Test hotels names")
    def test_names_hotels(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel = SearchHotelPage(self.driver)
        search_hotel.set_city_name("Dubai")
        search_hotel.set_date("12/09/2020", "15/09/2020")
        search_hotel.set_number_travelers("4", "1")
        search_hotel.click_search_button()
        return_hotel = ReturnHotelPage(self.driver)
        hotel_names = return_hotel.get_names_of_hotels()
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"

    @allure.title("Start test")
    @allure.feature("Feature")
    @allure.story("Story")
    @allure.description("Test hotels names")
    def test_prices_hotels(self, setup):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel = SearchHotelPage(self.driver)
        search_hotel.set_city_name("Dubai")
        search_hotel.set_date("12/09/2020", "15/09/2020")
        search_hotel.set_number_travelers("4", "1")
        search_hotel.click_search_button()
        return_hotel = ReturnHotelPage(self.driver)
        hotel_prices = return_hotel.get_prices_of_hotels()
        assert hotel_prices[0] == "€20.24"
        assert hotel_prices[1] == "€46"
        assert hotel_prices[2] == "€73.60"
        assert hotel_prices[3] == "€138"

# pytest --alluredir=report
# allure serve C:\Users\User\PycharmProjects\LEARNETIC\report
