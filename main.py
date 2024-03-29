import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from core.action.core import ActionCore
from core.instruction import Pattern
from core.instruction.pattern import PagePattern, MousePattern, KeyboardPattern
from core.page.page_object import *
from core.page.page_object import Page
from core.wait.waiter import WaitElementClick, WaitElementsClick
from sites.google import Google, GoogleSearch
from sites.google.google_search.locator import GoogleSearchLocator

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


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.set_script_timeout(300)
    driver.implicitly_wait(10)
    core_pattern = Pattern(
        mouse=MousePattern(
            speed=(0.1, 0.5),
            delay_before=(0.1, 0.5),
            delay_after=(0.3, 0.5)
        ),
        keyboard=KeyboardPattern(
            delay_before=(0.1, 0.5),
            delay_after=(0.3, 0.5),
            delay_send=(0.05, 0.3),
            delay_send_mistakes=(0.05, 0.1),
            change_mistakes=(0.05, 0.1)
        ),
        page=PagePattern(
            delay_before=(0.1, 0.5),
            delay_after=(0.3, 0.5),
        )
    )

    google = Google(
        driver=driver,
        pattern=core_pattern
    ).get().cookie_accept()

    try:
        while True:
            google.new_tab().get()
            page = random.choice(page for page, urls in Page.pages.items() if driver.current_url in urls)
            # page.
    finally:
        driver.quit()
