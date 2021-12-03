from .base import Pattern, _RangeFloat, _RangeInt


class PagePattern(Pattern):
    def __init__(self,
                 delay_before: _RangeFloat,
                 delay_after: _RangeFloat,
                 scroll_power_range: _RangeInt = (50, 1500),
                 scroll_sleep_range: _RangeFloat = (0.1, 1)):
        super().__init__(delay_before, delay_after)
        self.scroll_power_range = scroll_power_range
        self.scroll_sleep_range = scroll_sleep_range
