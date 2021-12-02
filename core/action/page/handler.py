import random

from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.action.page.action import PageAction

from core.action.page.locator import ElementPageLocator

from core.scripts.jinja_javascript import Scripts


class PageHandler:
    def __init__(self, driver: Remote):
        self.driver = driver

        self._page_action = PageAction(driver)
        self._locator = ElementPageLocator

    def scroll_on_element(self,
                          element: WebElement,
                          scrolling_power_range: list | tuple = (30, 2000),
                          scrolling_sleep_range: list | tuple = (400, 1800),
                          scrolling_element: WebElement = None,
                          blocked_elements: list[WebElement] = None
                          ):
        scrolling_element = scrolling_element or element.parent.find_element(By.TAG_NAME, "html")
        locator = self._locator(
            element=element, scrolling_element=scrolling_element,
            blocked_elements=blocked_elements)
        if locator.current_scrolling in range(*locator.limit.values()):
            return
        needed_scroll = locator.scroll_power
        self.driver.execute_async_script(
            Scripts.smooth_scroll,
            scrolling_element,
            needed_scroll,
            scrolling_power_range,
            scrolling_sleep_range)
