import pytest
from selenium import webdriver
@pytest.fixture
def test_setup():
    global driver
    driver = webdriver.Chrome()
    driver.get("C:\\Users\\User\\PycharmProjects\\LEARNETIC\\learn\\selenium\\resources\\Test.html")
    driver.maximize_window()
    yield
    driver.quit()

def  test_method(test_setup):
    assert driver.title == "Strona testowa"

def  test_method2(test_setup):
    assert driver.title == "Strona testowa"