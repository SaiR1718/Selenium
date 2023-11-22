from selenium import webdriver

class WebDriverFactory:
    @staticmethod
    def create_driver(browser):
        if browser == 'chrome':
            return webdriver.Chrome()
        elif browser == 'firefox':
            return webdriver.Firefox()
        # Add support for other browsers as needed
        else:
            raise Exception(f"Unsupported browser: {browser}")