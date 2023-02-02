class ExamException(Exception):
    pass
    
class CSVFile:
    def __init__(self, name):
        # Setto il nome del file
        self.name = name
        # Provo ad aprirlo e a leggere una riga
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except ExamException as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    def get_data(self):
        if not self.can_read:
            # Se can_read è settato a False, significa che il file non poteva essere aperto o era illeggibile
            print('Errore, file non aperto o illeggibile')

            # Esco dalla funzione tornando "None"
            return None
            
        else:
            # Inizializzo una lista vuota denominata 'data' per salvare tutti i dati
            data = []

            # Riapro il file, per leggere dalla prima riga (altrimenti proseguirei saltandola)
            my_file = open(self.name, 'r')

            # Con il ciclo 'for' leggo il file linea per linea
            for line in my_file:

                # Faccio lo split di ogni linea sulla virgola
                elements = line.split(',')

                # Utilizzo la funzione strip() per pulire il carattere di newline dall'ultimo elemento (e se ci sono, anche gli spazi bianchi posti all'inizio e alla fine)
                elements[-1] = elements[-1].strip()

                # Aggiungo gli elementi della linea alla lista (se non sto processando l'intestazione)
                if elements[0] != 'epoch':
                    data.append(elements)

            # Chiudo il file
            my_file.close()

            # Alla fine, quando ho processato tutte le righe, ritorno tutti i dati salvati nella lista 'data'
            return data

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        # Chiamo il metodo get_data del genitore 
        string_data = super().get_data()

        # Se lista è vuota, alzo un'eccezione
        if string_data == []:
            raise ExamException('Errore: lista valori vuota')

        # Preparo una lista per contenere i dati
        numerical_data = []

        # Con il ciclo for, voglio ottenere il primo epoch (così da poter controllare in seguito se i timestamp sono ordinati)
        for z, couple in enumerate(string_data):
            # Con una variabile ausiliaria, seleziono il primo elemento della string_data, cioè la prima linea
            first_line = string_data[z]
            
            # Controllo che sia possibile convertire il primo elemento della 'first_line' (adesso di tipo stringa) a valore numerico
            try:
                # Provo a convertirlo a float, e poi a intero
                int(float(first_line[0]))
                # Se ciò è possibile, interrompo il ciclo
                break

            # Se il primo elemento non è convertibile, passo all'elemento successivo
            except Exception:
                pass

        # Denomino il primo elemento della prima linea come 'epoch precedente' (dopo averlo convertito in un valore numerico, e più specificatamente, intero)
        previous_epoch = int(float(first_line[0]))

        # Assegno il valore dell'epoch precedente ad una nuova variabile, chiamata 'primo epoch'
        first_epoch = previous_epoch

        # Creo una variabile booleana per controllare ad ogni riga se ho due valori (epoch e temperatura), settandola a False (quindi ipotizzando di non averli)
        i_have_two_values = False

        # Ciclo su tutte le righe del file originale 
        for string_row in string_data:
            # Preparo una lista di supporto per salvare la riga in "formato" numerico
            numerical_row = []

            # Ciclo su tutti gli elementi della riga con un enumeratore, cosi da avere l'indice "i" della posizione dell'elemento
            for i, element in enumerate(string_row):
                # Controllo i timestamp (che si dovrebbero trovare nella prima posizione, i = 0)
                if i == 0:
                    try:
                        # Controllo che sia possibile convertire il primo elemento della lista (adesso di tipo stringa) a valore numerico (e specificatamente, intero), e in caso affermativo lo aggiungo alla riga
                        element = int(float(element))
                        numerical_row.append(element)

                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

                    # Se l'elemento non è il primo timestamp...
                    if element != first_epoch:

                        # Con la variabile 'previous_epoch' (creata precedentemente), controllo se il timestamp è minore del precedente e nel caso alzo un'eccezione
                        if element < previous_epoch:
                            raise ExamException('Errore: timestamp fuori ordine')
                            
                        # Analogamente, se il timestamp è uguale a quello precedente
                        if element == previous_epoch:
                            raise ExamException('Errore: timestamp duplicato')

                    # Adesso l'epoch precedente diventa quello "corrente"
                    previous_epoch = int(float(string_row[0]))

                # Controllo le temperature (che si dovrebbero trovare nella seconda posizione, i = 1)
                elif i == 1:
                     # Provo a convertire a float gli elementi. Se fallisco, stampo l'errore e rompo il ciclo.
                    try:
                        element = float(element)
                        if element != 0.0:
                            numerical_row.append(element)
                            # Se sono arrivato a questo punto, significa che ho due valori: posso settare la variabile a True
                            i_have_two_values = True
                        
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break
                        

                # Se ho ulteriori elementi nella stessa riga (i > 1), non li controllo, non aggiungendoli alla lista
                else:
                    pass


            # Alla fine aggiungo la riga in formato numerico alla lista "esterna", ma solo se sono riuscita a processare i due elementi (epoch e temperatura).
            if i_have_two_values:
                numerical_data.append(numerical_row)

            # Setto nuovamente la variabile a False e ricomincio il ciclo
            i_have_two_values = False
        
        return numerical_data

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

def compute_daily_max_difference(time_series):
     # Se lista è vuota, alzo un'eccezione
    if time_series == []:
        raise ExamException('Errore: lista valori vuota')
    
    # Creo la lista che conterrà le escursioni termiche
    temperature_range_list = []

    ## Setto alcune variabili di supporto (booleane e numeriche):
    # daily_measurements e index: per contare quante misurazioni giornaliere per una certa giornata sono presenti nel file
    daily_measurements = 0
    index = 1

    # counted: per controllare se ho già contato le misurazioni giornaliere di quella giornata
    counted = False

    #single_measurement: per verificare se ho una singola misurazione in quella giornata
    single_measurement = True
    

    # Inizio un ciclo for per controllare ogni riga
    for i, line in enumerate(time_series):
        # Se mi trovo nella prima riga o la variabile single_measurement è vera, imposto come temperatura massima e temperatura minima la temperatura di quel timestamp
        if i == 0 or single_measurement:
            max_temperature = line[1]
            min_temperature = line[1]

        # Calcolo l’inizio del giorno a cui appartiene l'epoch che sto controllando
        day_start_current_epoch = line[0] - (line[0] % 86400)

        #CONTO QUANTE MISURAZIONE DELLA TEMPERATURA CI SONO AL GIORNO
        # Se non ho (ancora) contato le misurazioni giornaliere di una giornata, le calcolo con un ciclo for:
        if not counted:
            for j, temporary_line in enumerate(time_series):
                # Di ogni epoch presente nella time_series, calcolo l'inizio del giorno
                day_start_temporary_epoch = temporary_line[0] - (temporary_line[0] % 86400)
                #Se esso coincide con l'inizio del giorno dell'epoch "corrente" (quello che sto controllando al di fuori di questo ciclo for), significa che i due timestamp appartengono alla stessa giornata
                if day_start_current_epoch == day_start_temporary_epoch:

                    # Posso quindi incrementare il numero di misurazioni giornaliere
                    daily_measurements = daily_measurements + 1;
            # Avendo quindi contato le misurazioni giornaliere, alla fine del ciclo setto counted a True
            counted = True

        # Se ho calcolato una (singola) misurazione, setto single_measurement a True
        if daily_measurements == 1:
            single_measurement == True


        # Se l'index è minore delle misurazioni giornaliere e non sono arrivata ancora in fondo alla lista, significa che mi trovo nella stessa giornata:
        if index < daily_measurements and i <= len(time_series):
            # Per questa giornata non ho una singola misurazione: posso settare single_measurement a False
            single_measurement = False

            # Controllo le temperature di questo timestamp e se sono minori o maggiori della temperatura minima/massima, assegno alle variabili il nuovo valore
            if line[1] > max_temperature:
                max_temperature = line[1]
            if line[1] < min_temperature:
                min_temperature = line[1]

        # Non mi trovo più nella stessa giornata: controllo se ho una misurazione singola o meno:
        else:
            if single_measurement:
                # Se ho una misurazione singola, aggiungo alla lista dei risultati il valore “None” per quella giornata, in quanto la differenza massima di una sola misurazione non è definita
                temperature_range_list.append(None)
                
            else:
                # Ricontrollo le temperature di questo timestamp (in quanto potrei essere arrivata alla fine della lista ma l'ultima misurazione è il valore massimo o minimo di quella giornata; in questo caso, devo assegnare alle variabili delle temperature il nuovo valore)
                if line[1] > max_temperature:
                    max_temperature = line[1]
                if line[1] < min_temperature:
                    min_temperature = line[1]

                # Calcolo l'escursione termica e aggiungo il suo valore alla lista
                range = max_temperature - min_temperature
                temperature_range_list.append(range)

                # Controllo se sono arrivata alla fine della lista (siccome il contatore 'i' parte da zero, calcolo la lunghezza della lista e sottraggo 1)
                if i == len(time_series) - 1:
                    # Se sono arrivato alla fine, restituisco la lista
                    return temperature_range_list
            
                else:
                    # Se sono arrivata alla fine della lista, calcolo il nuovo inizio della giornata dell'epoch "corrente"
                    day_start_current_epoch = line[0] - (line[0] % 86400)

                    # Imposto single_measurement a True (ipotizzando nuovamente di avere una singola misurazione)
                    single_measurement = True

            # Essendo arrivato al termine della giornata, resetto le variabili 'index' e 'daily_measurements', ponendole a 0, e setto counted a False, siccome non ho (ancora) contato le misurazioni giornaliere della nuova giornata
            index = 0
            daily_measurements = 0
            counted = False

        # Aumento il contatore 'index' di 1
        index = index + 1

    return temperature_range_list