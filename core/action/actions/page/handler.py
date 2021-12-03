from selenium.webdriver import Remote
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from core.action.actions.base import BaseHandler
from core.action.actions.page.action import PageAction

from core.action.actions.page.locator import ElementPageLocator

from core.instruction.pattern import PagePattern

from core.scripts.jinja_javascript import Scripts

_sec_to_ms = 1000


class PageHandler(BaseHandler):
    driver: Remote
    pattern: PagePattern

    _locator = ElementPageLocator


    def __init__(self, driver: Remote, pattern: PagePattern):
        super(PageHandler, self).__init__(driver, pattern)

        self._page_action = PageAction(driver)

    @BaseHandler.decorator_pattern_delays
    def scroll_to_element(self,
                          element: WebElement,
                          scrolling_element: WebElement = None,
                          blocked_elements: list[WebElement] = None
                          ):
        scrolling_element = scrolling_element or self.driver.find_element(By.TAG_NAME, "html")
        scroll_sleep_range = (*map(lambda x: int(x * _sec_to_ms), self.pattern.scroll_sleep_range),)
        scroll_power_range = self.pattern.scroll_power_range

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
            scroll_sleep_range,
            scroll_power_range)
