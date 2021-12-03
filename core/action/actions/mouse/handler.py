from selenium.webdriver import Remote

from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.remote.webelement import WebElement

from core.action.actions.base import BaseHandler
from core.action.actions.mouse.action import MouseAction

from core.action.actions.mouse.locator import ElementMouseLocator
from core.instruction.pattern import MousePattern

_sec_to_ms = 1000


class MouseHandler(BaseHandler):
    driver: Remote
    pattern: MousePattern

    _locator = ElementMouseLocator

    def __init__(self, driver: Remote, pattern: MousePattern):
        super(MouseHandler, self).__init__(driver, pattern)

        action = ActionBuilder(driver)
        self._mouse_action = MouseAction(action)

    @property
    def location(self):
        return self._mouse_action.location

    @BaseHandler.decorator_pattern_delays
    def move_to_element(self, element: WebElement, blocked_elements: list[WebElement] = None):
        speed = int(self.pattern.speed * _sec_to_ms)
        x, y = self._locator(element=element, blocked_elements=blocked_elements).xy
        self._mouse_action.move_to(speed, x, y)

    @BaseHandler.decorator_pattern_delays
    def click(self):
        self._mouse_action.click()

    @BaseHandler.decorator_pattern_delays
    def hold(self):
        self._mouse_action.hold()

    @BaseHandler.decorator_pattern_delays
    def release(self):
        self._mouse_action.release()
