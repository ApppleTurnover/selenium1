import time

from functools import wraps
from abc import ABC, abstractmethod


class BaseHandler(ABC):
    @abstractmethod
    def __init__(self, driver, pattern):
        self.driver = driver
        self.pattern = pattern

    @staticmethod
    def decorator_pattern_delays(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            time.sleep(self.pattern.delay_before)
            func(self, *args, **kwargs)
            time.sleep(self.pattern.delay_after)

        return wrapper
