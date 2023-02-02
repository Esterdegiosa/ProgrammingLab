class MyPower:
    def __init__(self, a):
        self.a = a

    def iteratore(self, a):
        for i in range(1, a + 1):
            x = pow(3, i + 1)/i
            print("f({}) vale {}" .format(i, x))

    def mean_pow_a(self):
        mean()
        
numero1 = MyPower(4)  
print(numero1.iteratore(4))