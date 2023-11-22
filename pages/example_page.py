from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class ExamplePage(BasePage):
    # Locators
    EXAMPLE_ELEMENT = (By.ID,"nav-logo-sprites")

    # Page Methods
    def click_example_element(self):
        self.driver.find_element(*self.EXAMPLE_ELEMENT).click()