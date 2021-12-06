from selenium.webdriver.common.by import By

from core.locator import Location as lc


class GoogleSearchLocator:
    search_input = lc(By.XPATH, "//input[@name='q']")
    cookie_accept = lc(By.XPATH, "//button[2]")
    search_form = lc(By.ID, "searchform")
    top_nav = lc(By.ID, "top_nav")
    links = lc(By.XPATH, "//a[h3]")
    ads = lc(By.XPATH, "//*[contains(@id, 'tads')]//a[br]")
