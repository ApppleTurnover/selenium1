from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

from core.instruction.pattern import Pattern


@dataclass
class PageObject:
    driver: webdriver.Remote
    scrolling_element: WebElement
    blocked_elements: list[WebElement]
    pattern: Pattern
