import time

from core.action.mouse.handler import MouseHandler
from core.action.page.handler import PageHandler
from core.action.keyboard.handler import KeyboardHandler


class ActionCore:
    def __init__(self, page_object):
        self.page_object = page_object

        self._mouse_handler = MouseHandler(page_object.driver)
        self._keyboard_handler = KeyboardHandler(page_object.driver)
        self._page_handler = PageHandler(page_object.driver)

    def pause(self, delay):
        time.sleep(delay)
        return self

    def scroll_on_element(self, element):
        self.pause(
            delay=self.page_object.pattern.scroll.delay_before
        )._page_handler.scroll_on_element(
            element=element,
            scrolling_element=self.page_object.scrolling_element,
            blocked_elements=self.page_object.blocked_elements,
            scrolling_power_range=self.page_object.pattern.scroll.power_range,
            scrolling_sleep_range=self.page_object.pattern.scroll.sleep_range
        )
        self.pause(self.page_object.pattern.scroll.delay_after)
        return self

    def move_on_element(self, element):
        self.scroll_on_element(
            element=element
        ).pause(
            delay=self.page_object.pattern.mouse.delay_before
        )._mouse_handler.move_on_element(
            element=element,
            blocked_elements=self.page_object.blocked_elements,
            ms=self.page_object.pattern.mouse.speed,
        )
        self.pause(self.page_object.pattern.mouse.delay_after)
        return self

    def click_on_element(self, element):
        self.move_on_element(
            element=element
        ).pause(
            self.page_object.pattern.mouse.delay_before
        )._mouse_handler.click()
        self.pause(self.page_object.pattern.mouse.delay_after)
        return self
