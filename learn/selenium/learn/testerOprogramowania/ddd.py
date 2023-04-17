import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGoogleSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome() # tutaj wybieramy przeglądarkę, np. Chrome
        self.driver.maximize_window() # maksymalizujemy okno przeglądarki

    def test_search(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title) # sprawdzamy, czy tytuł strony zawiera słowo "Google"
        self.driver.find_element(By.ID, "L2AGLb").click()
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium Python") # wpisujemy frazę "Selenium Python" w pole wyszukiwania
        search_box.send_keys(Keys.RETURN)
        wait = WebDriverWait(self.driver, 10)
        results = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.g")))
        self.assertGreater(len(results), 0) # sprawdzamy, czy znaleziono jakieś wyniki

    def tearDown(self):
        self.driver.quit() # zamykamy przeglądarkę

if __name__ == "__main__":
    unittest.main()