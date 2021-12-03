import random

from .base import Pattern, _RangeFloat, _is_range


class KeyboardPattern(Pattern):
    def __init__(self,
                 delay_before: _RangeFloat,
                 delay_after: _RangeFloat,
                 delay_send: _RangeFloat,
                 delay_send_mistakes: _RangeFloat,
                 change_mistakes: _RangeFloat):
        super().__init__(delay_before, delay_after)
        self.delay_send = delay_send
        self.delay_send_mistakes = delay_send_mistakes
        self.change_mistakes = change_mistakes

    @property
    def delay_send(self) -> float:
        return random.uniform(*self._delay_send)

    @delay_send.setter
    def delay_send(self, value: _RangeFloat):
        _is_range(value)
        self._delay_send = value

    @property
    def delay_send_mistakes(self) -> float:
        return random.uniform(*self._delay_send_mistakes)

    @delay_send_mistakes.setter
    def delay_send_mistakes(self, value: _RangeFloat):
        _is_range(value)
        self._delay_send_mistakes = value

    @property
    def change_mistakes(self) -> float:
        return random.uniform(*self._change_mistakes)

    @change_mistakes.setter
    def change_mistakes(self, value: _RangeFloat):
        _is_range(value)
        self._change_mistakes = value
