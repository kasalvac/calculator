import math


class Calculator:
    """is definition of a basic calculator"""

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def add(self): return self.a + self.b

    def subtract(self): return self.a - self.b


class CalculatorAdvanced(Calculator):
    def multiply(self): return self.a * self.b

    def divide(self): return self.a / self.b


class CalculatorExtreme(CalculatorAdvanced):
    def __init__(self, a=None, b=None, c=None):
        super().__init__(a, b)
        self.c = c

    def add_three(self): return self.a + self.b + self.c
