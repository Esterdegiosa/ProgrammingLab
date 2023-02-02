import math
class Function:
    def eval(self, x):
        pass

    def calcola_media(self, a, b, n):
        somma = 0
        variabile = (b - a)/(n - 1)
        for i in range (1, n + 1):
            somma = somma + self.eval(a + variabile * (i - 1))

        return 1/n * somma

class Retta(Function):
    def eval(self, x, m, q):
        return self.m * x + self.q
        
class Parabola(Function):
    def eval(self, x, a, b, c):
        return a * x ** 2 + b * x + self.c

class Iperbole(Function):
    def eval(self, x, a, b):
        argomento = (x * b ** 2)/(a ** 2) - (b ** 2)
        return math.sqrt(argomento)

retta1 = Retta(3, 2)
print(retta1.calcola_media(5, 2, 10000))