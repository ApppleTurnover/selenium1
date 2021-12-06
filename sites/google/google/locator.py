from selenium.webdriver.common.by import By

from core.locator import Location as lc


class GoogleLocator:
    search_input = lc(By.XPATH, "//input[@name='q']")
    cookie_accept = lc(By.XPATH, "//button[2]")
