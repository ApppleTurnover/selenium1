import random
from abc import ABCMeta, abstractmethod, ABC
from typing import TypeAlias

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from core.action.core import ActionCore
from core.instruction.pattern import Pattern
from core.page.url_object import URLs

driver_type: TypeAlias = webdriver.Remote
pattern_type: TypeAlias = Pattern
scrolling_element_type: TypeAlias = WebElement
blocked_elements_type: TypeAlias = list[WebElement]


class Page(ABCMeta):
    pages = {}

    @staticmethod
    def _all_bases(current_bases):
        bases = set()
        for current_base in current_bases:
            if isinstance(current_base, Page):
                bases |= Page._all_bases(current_base.__bases__)
                bases.add(current_base)
        return set(bases)

    def __init__(cls, name, bases, attrs):
        urls = attrs.get('urls')
        if urls and (urls is not ...):
            bases = Page._all_bases(bases)
            for base in bases:
                if not base.pages:
                    base.pages = {}
                pages = {cls: urls}
                base.pages.update(pages)

        super().__init__(name, bases, attrs)

    # def


class BasePageObject(metaclass=Page):
    urls: URLs = ...

    def __init__(self,
                 driver: driver_type,
                 pattern: pattern_type,
                 scrolling_element: scrolling_element_type = None,
                 blocked_elements: blocked_elements_type = None,
                 ):
        self.driver = driver
        self.pattern = pattern
        self.scrolling_element = scrolling_element
        self.blocked_elements = blocked_elements

        self.action = ActionCore(self)

    def get(self):
        self.driver.get(random.choice(self.urls))
        return self

    def setting(self,
                pattern: pattern_type,
                scrolling_element: scrolling_element_type = None,
                blocked_elements: blocked_elements_type = None,
                ):
        self.pattern = pattern
        self.scrolling_element = scrolling_element,
        self.blocked_elements = blocked_elements
        return self

    def pause(self, delay):
        self.action.pause(delay)
        return self

    @abstractmethod
    def automation(self): ...


class NewTabPageObject(BasePageObject, ABC):
    urls: URLs = ...

    def __init__(self,
                 driver: driver_type,
                 pattern: pattern_type,
                 scrolling_element: scrolling_element_type = None,
                 blocked_elements: blocked_elements_type = None
                 ):
        super().__init__(
            driver=driver,
            pattern=pattern,
            scrolling_element=scrolling_element,
            blocked_elements=blocked_elements
        )

        self._previous_window = driver.current_window_handle
        self._current_window = self.driver.current_window_handle

    def new_tab(self):
        self.driver.switch_to.new_window()
        self._current_window = self.driver.current_window_handle
        return self

    def close_tab(self):
        self.driver.switch_to.window(
            self._current_window)
        self.driver.close()
        self.driver.switch_to.window(
            self._previous_window)
        return self


class SomePage(BasePageObject, ABC):
    pass


__all__ = (
    "BasePageObject", "NewTabPageObject",
    "driver_type", "pattern_type",
    "scrolling_element_type", "blocked_elements_type"
)
