#Funziona (in teoria)
class Function:
    def eval(self, x):
        pass

    def f_hat(self, a, b, N):
        sum = 0
        v = (b - a)/N
        for i in range(N):
             sum = sum + self.eval(a + i * v)

        return sum / N

class Parabola(Function):
    def eval(self, x):
        return x * (x + 2)

parabola1 = Parabola()
print(parabola1.f_hat(1, 3, 3))

parabola2 = Parabola()
print(parabola2.f_hat(0, 6, 2))