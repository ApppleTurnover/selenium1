from dataclasses import dataclass

from core.instruction.pattern.patterns import MousePattern, PagePattern, KeyboardPattern


@dataclass
class Pattern:
    mouse: MousePattern
    keyboard: KeyboardPattern
    page: PagePattern
