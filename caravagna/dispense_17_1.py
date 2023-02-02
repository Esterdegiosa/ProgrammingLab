class Polinomi:
    def eval(self, x):
        pass

    def massimo(self, a, b):
        mass = max(self.eval(self,x))
        return mass
        
class PrimoGrado(Polinomi):
    def eval(self, x):
        return 2 * x + 1

class SecondoGrado(Polinomi):
    def eval(self, x):
        return x**x - 2 * x + 1

polinomio1 = PrimoGrado()
#print(polinomio1.eval(5))
print(polinomio1.massimo(3, 5))