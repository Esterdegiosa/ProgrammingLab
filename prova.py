class Persona:
    ruolo = "Studente UNITS"
    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome

    def bonjour(self):
        print(self.ruolo, ":", self.nome, self.cognome)

class Studente(Persona):
    def __init__(self, nome, cognome, lista_corsi):
        super().__init__("Studente UNITS", nome, cognome)
        self.lista_corsi = lista_corsi
        self.n = len(lista_corsi)
        
    def bonjour(self):
        Persona.bonjour(self)

    x = range(self.n)
    for i in x:
        print("Frequento il corso: ", self.lista_corsi[i])

lista_corsi = ["matematica generale", "analisi dati", "informatica"]
studente = Studente("Ester", "De Giosa", lista_corsi)


   def __init__(self, a, b, n):
        self.a = a
        self.b = b
        self.n = n