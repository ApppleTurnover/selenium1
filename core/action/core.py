import time

from selenium.webdriver.common.keys import Keys

from core.action.actions.mouse.handler import MouseHandler
from core.action.actions.page.handler import PageHandler
from core.action.actions.keyboard.handler import KeyboardHandler


class ActionCore:
    def __init__(self, page_object):
        self.page_object = page_object

        driver, pattern = page_object.driver, page_object.pattern

        self._mouse_handler = MouseHandler(driver, pattern.mouse)
        self._keyboard_handler = KeyboardHandler(driver, pattern.keyboard)
        self._page_handler = PageHandler(driver, pattern.page)

    def pause(self, delay):
        time.sleep(delay)
        return self

    def scroll_to_element(self, element):
        self._page_handler.scroll_to_element(
            element=element,
            scrolling_element=self.page_object.scrolling_element,
            blocked_elements=self.page_object.blocked_elements
        )
        return self

    def move_to_element(self, element):
        self.scroll_to_element(
            element=element
        )._mouse_handler.move_to_element(
            element=element,
            blocked_elements=self.page_object.blocked_elements
        )
        return self

    def click_on_element(self, element):
        self.move_to_element(
            element=element
        )._mouse_handler.click()
        return self

    def drag(self, element):
        self.move_to_element(
            element=element
        )._mouse_handler.hold()
        return self

    def drop(self, element):
        self.move_to_element(
            element=element
        )._mouse_handler.release()
        return self

    def drag_and_drop(self, drag_element, drop_element):
        self.drag(
            element=drag_element
        ).drop(
            element=drop_element
        )
        return self

    def write_text_to_element(self, element, text):
        self.move_to_element(
            element=element
        )._keyboard_handler.send_text(
            text=text
        )
        return self

    def send_text_to_element(self, element, text):
        self.write_text_to_element(
            element=element,
            text=text
        )._keyboard_handler.send_text(
            Keys.ENTER
        )
