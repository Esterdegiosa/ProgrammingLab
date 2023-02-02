#Funziona
class Rettangolo:
    def __init__(self, lunghezza, altezza):
        self.lunghezza = lunghezza
        self.altezza = altezza

    def perimetro(self, lunghezza, altezza):
        return 2 * lunghezza + 2 * altezza

    def area (self, lunghezza, altezza):
        return lunghezza * altezza

    def display(self, lunghezza, altezza):
        return 'lunghezza = ' + str(self.lunghezza) + '\naltezza = ' + str(self.altezza)

class Parallelepipedo(Rettangolo):
    def __init__(self, lunghezza, altezza, profondita):
        super().__init__(lunghezza, altezza)
        self.profondita = profondita

    def volume(self, lunghezza, altezza, profondita):
        return lunghezza * altezza * profondita

x = Rettangolo(5, 7)
print(x.display(5, 7))