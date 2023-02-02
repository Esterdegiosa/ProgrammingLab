class Veicolo:
    def __init__(self, modello, velocita, km):
        self.modello = modello
        self.velocita = velocita
        self.km = km

class Autobus(Veicolo):
    def __init__(self, modello, velocita, km, cm, rotta):
        super().__init__(modello, velocita, km)
        self.capienza_massima = cm
        self.rotta = rotta

    def informazioni(self, rotta):
        for citta in rotta:
            print(citta)

veicolo1 = Veicolo("auto fiat", "102", 10436)
autobus1 = Autobus("mod", "300", "10987", "30 posti", ["Milano", "Firenze", "Roma"])
print(autobus1.informazioni(["Milano", "Firenze", "Roma"]))