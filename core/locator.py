class Location:
    def __init__(self, by, value):
        self.by = by
        self.value = value

    def __format__(self, format_spec):
        value = self.value.format(format_spec)
        return value

    def format(self, format_spec):
        value = self.__format__(format_spec)
        return Location(self.by, value)

    def __iter__(self):
        return iter((self.by, self.value))

    def __add__(self, other):
        match other:
            case str():
                return Location(self.by, self.value + other)
            case Location():
                if other.by == self.by:
                    return Location(self.by, self.value + other.value)
                raise ValueError("Attributes 'by' don't match")
            case by, location:
                if by == self.by:
                    return Location(self.by, self.value + location)
                raise ValueError("Attributes 'by' don't match")
            case _:
                raise TypeError(f"Can't be added element with '{type(other)}'")

    def __repr__(self):
        return str((self.by, self.value))
