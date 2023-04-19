import allure
import pytest
from phptravels.pages.search_hotel_page import SearchHotelPage
from phptravels.pages.return_hotel_page import ReturnHotelPage
from phptravels.utils.read_excel import ExcelReader


@pytest.mark.usefixtures("setup")
class TestSearchHotel2:

    @allure.title("Start test")
    @allure.feature("Feature")
    @allure.story("Story")
    @allure.description("Test hotels names")
    @pytest.mark.parametrize("data", ExcelReader.get_data())
    def test_names_hotels(self, data):
        self.driver.get("http://www.kurs-selenium.pl/demo/")
        search_hotel = SearchHotelPage(self.driver)
        search_hotel.set_city_name("Dubai")
        search_hotel.set_date(data.checkin,data.checkout)
        search_hotel.set_number_travelers("4", "1")
        search_hotel.click_search_button()
        return_hotel = ReturnHotelPage(self.driver)
        hotel_names = return_hotel.get_names_of_hotels()
        assert hotel_names[0] == "Jumeirah Beach Hotel"
        assert hotel_names[1] == "Oasis Beach Tower"
        assert hotel_names[2] == "Rose Rayhaan Rotana"
        assert hotel_names[3] == "Hyatt Regency Perth"