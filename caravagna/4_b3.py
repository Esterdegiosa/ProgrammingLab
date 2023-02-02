class Obj:
    #def __init__(self, a, b, c):
     #   self.a = a
      #  self.b = b
       # self.c = c

    def eval(self, x, a, b, c):
        return a * x ** 2 + b * x + c
    
#def f1(x):
 #   return x**2 + 2*x
    
#def f2(x):
 #   return x**2 + 2*x - 1

o1 = Obj()
o2 = Obj()
print(o1.eval(1, 1, 2, 0))
print(o2.eval(1, 1, 2, -1))