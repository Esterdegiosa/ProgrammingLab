class C1:
    def __init__(self, i):
        self.i = i

    def quadrato(self, i):
        return i * i
        
class C2(C1):
    def __init__(self, i):
        super().__init__()
        self.i = 1

    def quadrato():
        pass

x = C2(5)
print(x.quadrato(5))