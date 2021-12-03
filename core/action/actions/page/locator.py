import random

import math

from selenium.webdriver.common.by import By

from selenium.webdriver.remote.webelement import WebElement

from core.scripts.jinja_javascript import Scripts


class ElementPageLocator:
    def __init__(self, element: WebElement, blocked_elements: list[WebElement] = None, scrolling_element: WebElement = None):
        self.element = element

        window_size = element.parent.execute_script(Scripts.get_window_size)
        self._window_height = window_size['height']
        self._window_width = window_size['width']

        self.blocked_elements = blocked_elements or []
        self.scrolling_element = scrolling_element or element.parent.find_element(By.TAG_NAME, "html")

    def get_limit_scrolling(self):
        rect = self.element.parent.execute_script(
            "return arguments[0].getBoundingClientRect()", self.element)
        y = rect['y'] + self.current_scrolling
        max_y = math.floor(y + rect['height'])
        min_y = math.ceil(y - self._window_height)
        return {
            "min_y": min_y, "max_y": max_y
        }

    def get_safe_location(self, min_y: int, max_y: int):
        rect = self.element.rect

        min_y = max(0, min_y)

        min_y += 3  # FROM MOUSE LOCATOR
        max_y -= 3  # FROM MOUSE LOCATOR

        min_x = math.ceil(rect['x'])
        max_x = min_x + math.floor(rect['width'])
        for element in self.blocked_elements:
            rect = element.parent.execute_script(Scripts.get_rect, element)

            blocked_min_x = rect['x']
            blocked_max_x = rect['x'] + rect['width']

            is_inside_x = lambda x: blocked_min_x <= x <= blocked_max_x

            if is_inside_x(min_x) and is_inside_x(max_x):
                if rect['bottom'] == self._window_height:
                    min_y += rect['height'] + 1
                else:
                    max_y -= rect['height'] + 1
        return {
            "min_y": min_y, "max_y": max_y
        }

    @property
    def current_scrolling(self):
        return self.element.parent.execute_script(
            "return arguments[0].scrollTop", self.scrolling_element)

    @property
    def min_y(self):
        limit = self.limit
        return limit['min_y']

    @property
    def max_y(self):
        limit = self.limit
        return limit['max_y']

    @property
    def limit(self):
        limit = self.get_safe_location(**self.get_limit_scrolling())
        return {
            "min_y": limit['min_y'], "max_y": limit['max_y']
        }

    @property
    def scroll_power(self):
        return random.randint(*self.limit.values())
