import random
import time
from dataclasses import dataclass

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionBuilder
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from core.action.core import ActionCore
from core.action.keyboard.action import KeyboardAction
from core.action.keyboard.handler import KeyboardHandler
from core.action.mouse.handler import MouseHandler
from core.action.mouse.locator import ElementMouseLocator
from core.action.page.handler import PageHandler
from core.action.page.locator import ElementPageLocator

mouse_view_script = r"""
function enableCursor() {
  var seleniumFollowerImg = document.createElement("img");
  seleniumFollowerImg.setAttribute('src', 'data:image/png;base64,'
    + 'iVBORw0KGgoAAAANSUhEUgAAABQAAAAeCAQAAACGG/bgAAAAAmJLR0QA/4ePzL8AAAAJcEhZcwAA'
    + 'HsYAAB7GAZEt8iwAAAAHdElNRQfgAwgMIwdxU/i7AAABZklEQVQ4y43TsU4UURSH8W+XmYwkS2I0'
    + '9CRKpKGhsvIJjG9giQmliHFZlkUIGnEF7KTiCagpsYHWhoTQaiUUxLixYZb5KAAZZhbunu7O/PKf'
    + 'e+fcA+/pqwb4DuximEqXhT4iI8dMpBWEsWsuGYdpZFttiLSSgTvhZ1W/SvfO1CvYdV1kPghV68a3'
    + '0zzUWZH5pBqEui7dnqlFmLoq0gxC1XfGZdoLal2kea8ahLoqKXNAJQBT2yJzwUTVt0bS6ANqy1ga'
    + 'VCEq/oVTtjji4hQVhhnlYBH4WIJV9vlkXLm+10R8oJb79Jl1j9UdazJRGpkrmNkSF9SOz2T71s7M'
    + 'SIfD2lmmfjGSRz3hK8l4w1P+bah/HJLN0sys2JSMZQB+jKo6KSc8vLlLn5ikzF4268Wg2+pPOWW6'
    + 'ONcpr3PrXy9VfS473M/D7H+TLmrqsXtOGctvxvMv2oVNP+Av0uHbzbxyJaywyUjx8TlnPY2YxqkD'
    + 'dAAAAABJRU5ErkJggg==');
  seleniumFollowerImg.setAttribute('id', 'selenium_mouse_follower');
  seleniumFollowerImg.setAttribute('style', 'position: absolute; z-index: 99999999999; pointer-events: none; left:0; top:0');
  document.body.appendChild(seleniumFollowerImg);
  document.onmousemove = function (e) {
    document.getElementById("selenium_mouse_follower").style.left = e.pageX + 'px';
    document.getElementById("selenium_mouse_follower").style.top = e.pageY + 'px';
  };
};
enableCursor();
"""


# def tjournal():
#     driver.find_element_by_css_selector(".propaganda[data-id='1']")
#
#     while driver.execute_script("return document.readyState") != "complete":
#         time.sleep(0.1)
#     time.sleep(5)
#
#     while element := random.choice(driver.find_elements_by_css_selector("a > time")):
#         driver.find_element_by_css_selector(".propaganda[data-id='1']")
#
#         header = driver.find_element_by_css_selector(".site-header")
#         try:
#             footer = driver.find_element_by_css_selector("#stratum")
#         except Exception:
#             footer = None
#
#         page_handler.scroll_on_element(
#             element=element,
#             blocked_elements=[header, footer] if footer else [header]
#         )
#         time.sleep(1)
#         mouse_handler.move_on_element(
#             ms=100, element=element,
#             blocked_elements=[header, footer] if footer else [header]
#         )
#         mouse_handler._mouse_action.click()
#         time.sleep(1)
#         driver.back()
#         time.sleep(2)
#
#         scrolling_element = driver.find_element_by_css_selector("html")
#         page_handler._page_action.page_up(scrolling_element, 1)
#         element.click()
#         time.sleep(5)
#         driver.back()
#         time.sleep(5)


class Mouse:
    speed = 100
    delay_before = 0.5
    delay_after = 0.5


class Keyboard:
    pass


class Scroll:
    delay_before = 0.5
    delay_after = 0.5
    power_range = [50, 1500]
    sleep_range = [100, 1000]


class Pattern:
    mouse = Mouse()
    keyboard = Keyboard()
    scroll = Scroll()


@dataclass
class PageObject:
    driver: webdriver.Remote
    scrolling_element: WebElement
    blocked_elements: list[WebElement]
    pattern = Pattern()


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.set_script_timeout(300)
    driver.implicitly_wait(10)
    driver.get(
        "https://www.google.com/search?q=google+news&source=lmns&tbm=nws&bih=882&biw=1745&hl=ru&sa=X&ved=2ahUKEwjl8Y-5wcL0AhWGuCoKHaHFBJcQ_AUoAXoECAEQAQ")
    driver.find_element_by_xpath("(//button)[2]").click()
    driver.execute_script(mouse_view_script)
    block_element = [driver.find_element_by_xpath("//body/div/div/form")]
    scrolling_element = driver.find_element_by_xpath("//html")
    action = ActionCore(page_object=PageObject(driver, scrolling_element, block_element))
    try:
        while True:
            element = random.choice(driver.find_elements_by_xpath("//g-card/div/div/a"))
            action.move_on_element(element)
    finally:
        driver.quit()
