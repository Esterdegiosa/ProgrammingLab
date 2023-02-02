class Vacanza:
    def __init__(self, nome, partenza, ritorno, localita, resort, prezzo, partecipanti, responsabile):
        self.nome = nome
        self.partenza = partenza
        self.ritorno = ritorno
        self.localita = localita
        self.resort = resort
        self.prezzo = prezzo
        self.partecipanti = partecipanti
        self.responsabile = responsabile

    def stampa(self):
        pass

    def periodo(self, partenza, ritorno):
        anni = ritorno[2] - partenza[2]
        mesi = ritorno[1] - partenza[1]
        giorni = ritorno[0] - partenza[0]
        print('Il periodo è durato: {} giorni, {} mesi e {} anni'.format(giorni, mesi, anni))

    def guadagno(self, prezzo):
        ricavo_netto = prezzo * 0.53
        return ricavo_netto

class VacanzaInvernale(Vacanza):
    def _init__(self, nome, partenza, ritorno, localita, resort, prezzo, partecipanti, responsabile, skipass, impianti):
        super().__init__(nome, partenza, ritorno, localita, resort, prezzo, partecipanti, responsabile)
        self.skipass = skipass
        self.impianti = impianti

    def guadagno(self, prezzo):
        ricavo_netto = prezzo * 0.53
        return ricavo_netto

class VacanzaEstiva(Vacanza):
    def _init__(self, nome, partenza, ritorno, localita, resort, prezzo, partecipanti, responsabile, distanza, escursioni):
        super().__init__(nome, partenza, ritorno, localita, resort, prezzo, partecipanti, responsabile)
        self.distanza = distanza
        self.escursioni = escursioni

vacanza1 = Vacanza("natura", [3, 4, 2022], [10, 4, 2022], "Roma", "il moro", "1000 $", ["Rossi", "Verdi", "Neri", "Bianchi"], "Mario Bianchi")
print(vacanza1.guadagno(1000)