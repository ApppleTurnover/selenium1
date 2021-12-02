import random
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from core.action.keyboard.action import KeyboardAction


class KeyboardHandler:
    def __init__(self, driver):
        self.driver = driver

        action = ActionBuilder(driver)

        self._keyboard_action = KeyboardAction(action)

    def send_text(self,
                  text: str,
                  delay_send: float,
                  delay_send_mistakes: float,
                  change_mistakes: float
                  ):
        for index, char in enumerate(text):
            count_miss = 0
            while random.random() < change_mistakes:
                if not index + count_miss >= len(text):
                    break
                erroneous_character = random.choice(text)
                self._keyboard_action.send_keys(erroneous_character)
                time.sleep(delay_send_mistakes)
                count_miss += 1
            else:
                self._keyboard_action.send_keys((Keys.BACKSPACE,) * count_miss)
                time.sleep(delay_send_mistakes)

            self._keyboard_action.send_keys(char)
            time.sleep(delay_send)


