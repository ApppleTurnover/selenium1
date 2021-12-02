from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.remote.webelement import WebElement

from core.action.mouse.action import MouseAction

from core.action.mouse.locator import ElementMouseLocator


class MouseHandler:
    def __init__(self, driver):
        self.driver = driver

        action = ActionBuilder(driver)

        self._mouse_action = MouseAction(action)
        self._locator = ElementMouseLocator

    @property
    def location(self):
        return self._mouse_action.location

    def move_on_element(self,
                        ms: int,
                        element: WebElement,
                        blocked_elements: list[WebElement] = None
                        ):
        x, y = self._locator(element=element, blocked_elements=blocked_elements).xy
        self._mouse_action.move_to(ms, x, y)

    def click(self):
        self._mouse_action.click()
