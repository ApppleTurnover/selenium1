import random

from .base import Pattern, _RangeFloat, _is_range


class MousePattern(Pattern):
    def __init__(self,
                 delay_before: _RangeFloat,
                 delay_after: _RangeFloat,
                 speed: _RangeFloat):
        super().__init__(delay_before, delay_after)
        self.speed = speed

    @property
    def speed(self) -> float:
        return random.uniform(*self._speed)

    @speed.setter
    def speed(self, value: _RangeFloat):
        _is_range(value)
        self._speed = value
