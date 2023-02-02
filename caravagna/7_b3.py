class SistemaPagamento:
    def calcola_pagamento(self, impiegati):
        print('Calcolo pagamento')
        print('===================')
        for impiegato in impiegati:
            print("Payroll:", impiegato.id,'-', impiegato.name)
            print("Totale:" impiegato.calcola_pagamento(), "\n")