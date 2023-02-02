#Funziona
import math
class Funzione:
    def eval(self, x):
        pass

    def calcola_integrale(self, a, b, M):
        h = (b - a)/M

        sum = 0
        for i in range(M):
            variabile = a + i * h
            sum = sum + self.eval(variabile)

        return sum * h
        #oppure: return h * sum([self.eval(a + i * h) for i in range(M)])

class Parabola(Funzione):
    def eval(self, x):
        return x * (x - 2)

class Esponenziale(Funzione):
    def eval(self, x):
        return pow(math.e, 2 * x)

class Frazionaria(Funzione):
    def eval(self, x):
        return x / (1 + x * x)

parabola1 = Parabola()
esponenziale1 = Esponenziale()
frazionaria1 = Frazionaria()

print(parabola1.calcola_integrale(0, 1, 100000))
print(esponenziale1.calcola_integrale(-math.pi/2, math.pi, 100000))
print(frazionaria1.calcola_integrale(-2, 2, 100000))