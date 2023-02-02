class Automobile:
    def __init__(self, name, casa_automo, modello, numero_posti, targa):
        self.name = name
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    def __str__(self, name, casa_automo, modello, numero_posti, targa):
        print(name)
        print(casa_automo)

    def parla(self):
        print("Broom Broom")

    def confronta(self):
        pass

auto1 = Automobile("lily", "fiat", "fiat 500", "4 posti", "AA111AA")
auto2 = Automobile("red", "fiat", "fiat 500", "4 posti", "BB222BB")
print(auto2.targa)