

class Dollars(float):
    """Represent a float as dollars."""
    def __repr__(self):
        return f"${self.__float__():,.2f}"

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        return Dollars(super().__add__(other))

    def __radd__(self, other):
        return Dollars(super().__radd__(other))