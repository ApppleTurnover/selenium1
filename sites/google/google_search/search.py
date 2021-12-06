import random

from core.page.page_object import BasePageObject
from core.page.url_object import URLs
from core.wait.waiter import WaitElementClick, WaitElementsClick
from sites.google.google_search.locator import GoogleSearchLocator


class GoogleSearch(BasePageObject):
    urls = URLs(
        "https://www.google.com/search"
    )

    def cookie_accept(self):
        self.action.click_on_element(
            element=WaitElementClick(
                driver=self.driver,
                delay_wait=40,
                locator=GoogleSearchLocator.cookie_accept
            )
        )
        return self

    def click_on_ads(self):
        self.action.click_on_element(
            element=WaitElementClick(
                driver=self.driver,
                delay_wait=40,
                locator=GoogleSearchLocator.ads
            )
        )
        return self

    def click_on_link(self):
        self.action.click_on_element(
            element=random.choice(
                WaitElementsClick(
                    driver=self.driver,
                    delay_wait=40,
                    locator=GoogleSearchLocator.links
                )
            )
        )
        return self

    def automation(self):
        self.click_on_link().pause(2)
