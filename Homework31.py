class Calculator:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Value must be an int or float.")
        self.__value = value

    @property
    def value(self):
        return self.__value

    def __add__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__value + other.value)
        elif isinstance(other, (int, float)):
            return Calculator(self.__value + other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __sub__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__value - other.value)
        elif isinstance(other, (int, float)):
            return Calculator(self.__value - other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __mul__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__value * other.value)
        elif isinstance(other, (int, float)):
            return Calculator(self.__value * other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __truediv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Calculator(self.__value / other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Calculator(self.__value / other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __floordiv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Calculator(self.__value // other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return Calculator(self.__value // other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __mod__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            return Calculator(self.__value % other.value)
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            return Calculator(self.__value % other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __pow__(self, other):
        if isinstance(other, Calculator):
            return Calculator(self.__value ** other.value)
        elif isinstance(other, (int, float)):
            return Calculator(self.__value ** other)
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __iadd__(self, other):
        if isinstance(other, Calculator):
            self.__value += other.value
        elif isinstance(other, (int, float)):
            self.__value += other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __isub__(self, other):
        if isinstance(other, Calculator):
            self.__value -= other.value
        elif isinstance(other, (int, float)):
            self.__value -= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __imul__(self, other):
        if isinstance(other, Calculator):
            self.__value *= other.value
        elif isinstance(other, (int, float)):
            self.__value *= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __itruediv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.__value /= other.value
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.__value /= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __ifloordiv__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.__value //= other.value
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            self.__value //= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __imod__(self, other):
        if isinstance(other, Calculator):
            if other.value == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            self.__value %= other.value
        elif isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError("Modulo by zero is not allowed.")
            self.__value %= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __ipow__(self, other):
        if isinstance(other, Calculator):
            self.__value **= other.value
        elif isinstance(other, (int, float)):
            self.__value **= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")
        return self

    def __eq__(self, other):
        if isinstance(other, Calculator):
            return self.__value == other.value
        elif isinstance(other, (int, float)):
            return self.__value == other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if isinstance(other, Calculator):
            return self.__value < other.value
        elif isinstance(other, (int, float)):
            return self.__value < other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __le__(self, other):
        if isinstance(other, Calculator):
            return self.__value <= other.value
        elif isinstance(other, (int, float)):
            return self.__value <= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __gt__(self, other):
        if isinstance(other, Calculator):
            return self.__value > other.value
        elif isinstance(other, (int, float)):
            return self.__value > other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __ge__(self, other):
        if isinstance(other, Calculator):
            return self.__value >= other.value
        elif isinstance(other, (int, float)):
            return self.__value >= other
        else:
            raise TypeError("Operand must be an int, float, or Calculator.")

    def __str__(self):
        return str(self.__value)

    def __repr__(self):
        return f"Calculator(value={self.__value}, type={type(self.__value).__name__})"

