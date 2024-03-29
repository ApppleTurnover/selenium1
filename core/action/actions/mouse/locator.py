import math
import random
import itertools

from selenium.webdriver.remote.webelement import WebElement

from core.exc import MouseLocationException
from core.scripts.jinja_javascript import Scripts


class ElementMouseLocator:
    def __init__(self, element: WebElement, blocked_elements: list[WebElement] = None):
        self.element = element

        window_size = element.parent.execute_script(Scripts.get_window_size)
        self._window_height = window_size['height']
        self._window_width = window_size['width']

        rect = element.rect

        self.width = rect['width']
        self.height = rect['height']

        self.blocked_elements = blocked_elements or []

    def get_limit(self) -> dict[str, int]:
        rect = self.element.parent.execute_script(Scripts.get_rect, self.element)

        min_x = math.ceil(rect['x'])
        max_x = min_x + math.floor(self.width)

        min_y = math.ceil(rect['y'])
        max_y = min_y + math.floor(self.height)

        return {
            "min_x": min_x,
            "min_y": min_y,
            "max_y": max_y,
            "max_x": max_x,
        }

    def get_safe_dots(self, min_x: int, min_y: int, max_x: int, max_y: int) -> tuple[tuple]:
        # TODO optimization is needed (1000x1000 points can be processed, which takes a lot of time)
        min_x = max(0, min_x) + 1
        max_x = min(self._window_width, max_x) - 1
        min_y = max(0, min_y) + 1
        max_y = min(self._window_height, max_y) - 1

        if any([
            max_x < 0 or max_y < 0,
            min_x >= self._window_width or min_y >= self._window_height,
            min_x >= max_x or min_y >= max_y
        ]):
            raise ValueError("The element is outside the window")

        dots_x = range(min_x, max_x)
        dots_y = range(min_y, max_y)
        dots = itertools.product(dots_x, dots_y)
        if not self.blocked_elements:
            return tuple(dots)

        get_rect = lambda el: el.parent.execute_script(Scripts.get_rect, el)
        blocked_rects = tuple(map(get_rect, self.blocked_elements))
        blocked_locators = tuple(map(lambda el:
                                     (range(math.ceil(el['x']) - 1,
                                            math.floor(el['x'] + el['width']) + 1),
                                      range(math.ceil(el['y']) - 1,
                                            math.floor(el['y'] + el['height']) + 1)),
                                     blocked_rects))

        for blocked_x, blocked_y in blocked_locators:
            dots = filter(
                lambda locator:
                locator[0] not in blocked_x or locator[1] not in blocked_y,
                dots
            )
        return tuple(dots)

    @property
    def xy(self):
        if not (safe_dots := self.get_safe_dots(**self.get_limit())):
            raise MouseLocationException("Element out of bounds")
        return random.choice(safe_dots)

    @property
    def x(self):
        x, y = self.xy
        return x

    @property
    def y(self):
        x, y = self.xy
        return y
