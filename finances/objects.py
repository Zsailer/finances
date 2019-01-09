from functools import wraps

# Monkey Patch Floats to behave like dollars. 
methods_to_monkey_patch = [
    '__add__',
    '__radd__',
    '__mul__',
    '__pow__',
    '__divmod__',
    '__rdivmod__',
    '__rmul__',
    '__round__',
    '__rpow__',
    '__rsub__',
    '__rtruediv__',
    '__sub__',
    '__truediv__',
]

class Dollars(float):
    """Represent a float as dollars.
    """
    def __repr__(self):
        return f"${self.__float__():,.2f}"

    def __str__(self):
        return self.__repr__()

    @wraps(float.__add__)
    def __add__(self, other):
        return Dollars(super().__add__(other))

    @wraps(float.__radd__)
    def __radd__(self, other):
        return Dollars(super().__radd__(other))

    @wraps(float.__mul__)
    def __mul__(self, other):
        return Dollars(super().__mul__(other))

    @wraps(float.__pow__)
    def __pow__(self, other):
        return Dollars(super().__pow__(other))

    @wraps(float.__divmod__)
    def __divmod__(self, other):
        return Dollars(super().__divmod__(other))

    @wraps(float.__rdivmod__)
    def __rdivmod__(self, other):
        return Dollars(super().__rdivmod__(other))

    @wraps(float.__rmul__)
    def __rmul__(self, other):
        return Dollars(super().__rmul__(other))

    @wraps(float.__rpow__)
    def __rpow__(self, other):
        return Dollars(super().__rpow__(other))

    @wraps(float.__rsub__)
    def __rsub__(self, other):
        return Dollars(super().__rsub__(other))

    @wraps(float.__rtruediv__)
    def __rtruediv__(self, other):
        return Dollars(super().__rtruediv__(other))

    @wraps(float.__sub__)
    def __sub__(self, other):
        return Dollars(super().__sub__(other))

    @wraps(float.__truediv__)
    def __truediv__(self, other):
        return Dollars(super().__truediv__(other))

    @wraps(float.__round__)
    def __round__(self, other):
        return Dollars(super().__round__(other))
