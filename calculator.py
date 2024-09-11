import math


class Calculator:
    """is definition of a basic calculator"""

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def add(self): return self.a + self.b

    def subtract(self): return self.a - self.b


data1 = Calculator(5, 7)

print(data1.add())


class CalculatorAdvanced(Calculator):
    def multiply(self): return self.a * self.b

    def divide(self): return self.a / self.b


data2 = CalculatorAdvanced(4, 6)

print(data2.subtract())
print(data2.multiply())


class CalculatorExtreme(CalculatorAdvanced):
    def __init__(self, a=None, b=None, c=None):
        super().__init__(a, b)
        self.c = c

    def add_three(self): return self.a + self.b + self.c


data3 = CalculatorExtreme(3, 2, 8)

print(data3.add_three())




