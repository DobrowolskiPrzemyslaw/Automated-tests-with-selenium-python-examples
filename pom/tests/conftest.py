import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver


@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_faild = request.session.testsfailed
    yield
    if request.session.testsfailed != before_faild:
        allure.attach(driver.get_screenshot_as_png(), name="set_city", attachment_type=AttachmentType.PNG)
    driver.quit()