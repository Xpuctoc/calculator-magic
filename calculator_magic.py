class Calculator:

    def __init__(self, init_value=0, attribute_limit=10):
        self.__dict__['value'] = init_value
        self.__dict__['attribute_limit'] = attribute_limit
        self.value = init_value
        self.attribute_limit = attribute_limit

    def __add__(self, other):
        value = self.value
        value += other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __sub__(self, other):
        value = self.value
        value -= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __mul__(self, other):
        value = self.value
        value *= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __truediv__(self, other):
        value = self.value
        value /= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __floordiv__(self, other):
        value = self.value
        value //= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __pow__(self, other):
        value = self.value
        value **= other.value if isinstance(other, Calculator) else other
        return Calculator(value)

    def __setattr__(self, key, value):
        if len(self.__dict__) >= self.attribute_limit:
            raise AttributeError
        self.__dict__[key] = value

    def __iter__(self):
        return self.value

    def __repr__(self):
        return str(self.value)

    def __str__(self):
        return str(self.__dict__)
