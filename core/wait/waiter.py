from abc import ABC

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ElementWaiter(ABC):
    ec_wait: EC = None

    def __new__(cls, driver, delay_wait, locator):
        element = WebDriverWait(driver, delay_wait).until(
            cls.ec_wait(locator))
        return WebElement(element.parent, element.id)


class WaitElementClick(ElementWaiter):
    ec_wait = EC.element_to_be_clickable


class WaitElementLocation(ElementWaiter):
    ec_wait = EC.presence_of_element_located


class ElementsWaiter(ABC):
    ec_wait: EC = None

    def __new__(cls, driver, delay_wait, locator):
        WebDriverWait(driver, delay_wait).until(
            cls.ec_wait(locator))
        return driver.find_elements(*locator)


class WaitElementsClick(ElementsWaiter):
    ec_wait = EC.element_to_be_clickable


class WaitElementsLocation(ElementsWaiter):
    ec_wait = EC.presence_of_element_located
