import random

import pytest

from selenium_demo.pages.my_accoutn_page import MyAccoutPage
from selenium_demo.pages.update_biling_adress_page import UpDateBilingAdressPage


@pytest.mark.usefixtures("setup")
class TestCreateAccount:
    def test_update_biling_address(self):
        email = f"eamil{random.randint(0, 10000)}@wp.pl"
        my_accout_page = MyAccoutPage(self.driver)
        my_accout_page.open_page()
        my_accout_page.create_account(email, "password")
        update_biling_adress_page = UpDateBilingAdressPage(self.driver)
        update_biling_adress_page.open_edit_biling_address()
        update_biling_adress_page.set_personal_data("Przemyslaw", "Dobrowola")
        update_biling_adress_page.select_country("Poland")
        update_biling_adress_page.set_adress("Kwiatowa","00-500","Gostyń")
        update_biling_adress_page.set_phone_number("0700")
        update_biling_adress_page.save_address()
        print(update_biling_adress_page.get_message())
        assert "Address changed successfully." in  update_biling_adress_page.get_message()