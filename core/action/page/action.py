from selenium.webdriver import Remote


class PageAction:
    def __init__(self, driver: Remote):
        self._driver = driver

    def back_page(self):
        self._driver.back()

    def close_page(self):
        self._driver.close()
