import allure
import pytest
from allure_commons.types import AttachmentType
from phptravels.utils.driver_factory import DriverFactory

@pytest.fixture()
def setup(request):
    driver = DriverFactory.get_driver("chrome")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    before_faild = request.session.testsfailed
    yield
    if request.session.testsfailed != before_faild:
        allure.attach(driver.get_screenshot_as_png(), name="test_failed", attachment_type=AttachmentType.PNG)
    driver.quit()