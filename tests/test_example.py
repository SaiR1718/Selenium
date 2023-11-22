import unittest
from config.config import Config
from utils.webdriver_factory import WebDriverFactory
from pages.example_page import ExamplePage

class TestExample(unittest.TestCase):
    def setUp(self):
        self.driver = WebDriverFactory.create_driver(Config.BROWSER)
        self.page = ExamplePage(self.driver)
        self.driver.maximize_window()

    def test_example(self):
        self.page.open_url(Config.BASE_URL)
        self.page.click_example_element()
        # Add assertions and further test steps as needed

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()