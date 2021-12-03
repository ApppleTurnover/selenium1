import random
import time

from selenium.webdriver import Remote
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.keys import Keys

from core.action.actions.base import BaseHandler
from core.action.actions.keyboard.action import KeyboardAction
from core.instruction.pattern import KeyboardPattern


class KeyboardHandler(BaseHandler):
    driver: Remote
    pattern: KeyboardPattern

    def __init__(self, driver: Remote, pattern: KeyboardPattern):
        super(KeyboardHandler, self).__init__(driver, pattern)

        action = ActionBuilder(driver)

        self._keyboard_action = KeyboardAction(action)

    @BaseHandler.decorator_pattern_delays
    def send_text(self, text: str):
        for index, char in enumerate(text):
            count_miss = 0
            while random.random() < self.pattern.change_mistakes:
                if not index + count_miss >= len(text):
                    break
                erroneous_character = random.choice(text)
                self._keyboard_action.send_keys(erroneous_character)
                time.sleep(self.pattern.delay_send_mistakes)
                count_miss += 1
            else:
                self._keyboard_action.send_keys((Keys.BACKSPACE,) * count_miss)
                time.sleep(self.pattern.delay_send_mistakes)

            self._keyboard_action.send_keys(char)
            time.sleep(self.pattern.delay_send)
