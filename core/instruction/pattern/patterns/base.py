import random

from abc import ABC
from typing import TypeAlias

_RangeFloat: TypeAlias = list[float, int] | tuple[float, int]
_RangeInt: TypeAlias = list[int] | tuple[int]


def _is_range(value):
    match value:
        case property():
            return
        case list() | tuple():
            if all((
                    len(value) == 2,
                    isinstance(value[0], int | float),
                    isinstance(value[1], int | float),
            )):
                return

    raise ValueError("It is necessary to pass the list | tuple from min to max")


class Pattern(ABC):
    def __init__(self, delay_before: _RangeFloat, delay_after: _RangeFloat):
        self.delay_before = delay_before
        self.delay_after = delay_after

    @property
    def delay_before(self) -> float:
        return random.uniform(*self._delay_before)

    @delay_before.setter
    def delay_before(self, value: _RangeFloat):
        _is_range(value)
        self._delay_before = value

    @property
    def delay_after(self) -> float:
        return random.uniform(*self._delay_after)

    @delay_after.setter
    def delay_after(self, value: _RangeFloat):
        _is_range(value)
        self._delay_after = value
