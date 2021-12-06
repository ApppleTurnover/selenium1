from core.page.page_object import NewTabPageObject, SomePage
from core.page.url_object import URLs
from core.wait.waiter import WaitElementClick
from sites.google.google.locator import GoogleLocator


class Google(NewTabPageObject, SomePage):
    urls = URLs(
        "https://www.google.com/",
        "https://www.google.com/webhp"
    )

    def cookie_accept(self):
        self.action.click_on_element(
            element=WaitElementClick(
                driver=self.driver,
                delay_wait=40,
                locator=GoogleLocator.cookie_accept
            )
        )
        return self

    def search(self, text):
        self.action.send_text_to_element(
            text=text,
            element=WaitElementClick(
                driver=self.driver,
                delay_wait=10,
                locator=GoogleLocator.search_input
            ),
        )
        return self

    def automation(self):
        self.search("Ads")
