#Dovrebbe funzionare
class Function:
    def eval(self, x):
        pass

class Retta(Function):
    #def __init__(self, m, q):
     #   self.m = m
      #  self.q = q
    
    def eval(self, x, m ,q):
        return m * x + q
    
class AbsoluteValueFunction(Retta):
    def eval(self, x, m ,q):
        r = super().eval(x, m ,q)
        return abs(r) #non funziona

retta1 = Retta()
retta2 = Retta()
print(retta1.eval(3, 2, -3))
print(retta2.eval(-4, 2, -1))