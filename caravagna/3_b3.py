class Veicolo:
    def __init__(self, p, v, km):
        self.posti = p
        self.velocita = self.v
        self.km = km

class Auto4(Veicolo):
    def __init__(self, v, km):
        super().__init__(self, v, km)

auto_4 = Auto4()
print(auto_4.velocita())