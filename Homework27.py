import math

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def side(self):
        return self.a, self.b, self.c

    def p(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.p() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def type(self):
        if self.a == self.b == self.c:
            return "Հավասարակողմ"
        elif self.a == self.b or self.b == self.c or self.a == self.c:
            return "Հավասարասրուն"
        else:
            return "Անկանոն"

    def C(self):
        return (self.a * self.b * self.c) / (4 * self.area())