class ExamException(Exception):
    pass
    
class CSVFile:
    def __init__(self, name):
        self.name = name
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))

    def get_data(self):
        if not self.can_read:
            print('Errore, file non aperto o illeggibile')
            return None          
        else:
            data = []
            my_file = open(self.name, 'r')
            for line in my_file:
                elements = line.split(',')
                elements[-1] = elements[-1].strip()
                if elements[0] != 'epoch':
                    data.append(elements)
            my_file.close()
            return data

class CSVTimeSeriesFile(CSVFile):
    def get_data(self):
        string_data = super().get_data()
        if string_data == []:
            raise ExamException('Errore: lista valori vuota')

        numerical_data = []
        for z, couple in enumerate(string_data):
            first_line = string_data[z]
            try:
                int(float(first_line[0]))
                break
            except Exception:
                pass
        previous_epoch = int(float(first_line[0]))
        first_epoch = previous_epoch
        i_have_two_values = False

        for string_row in string_data:
            numerical_row = []
            for i, element in enumerate(string_row):
                if i == 0:
                    try:
                        element = int(float(element))
                        numerical_row.append(element)
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

                    if element != first_epoch:
                        if element < previous_epoch:
                            raise ExamException('Errore: timestamp fuori ordine')
                        if element == previous_epoch:
                            raise ExamException('Errore: timestamp duplicato')
                    previous_epoch = int(float(string_row[0]))

                elif i == 1:
                    try:
                        element = float(element)
                        numerical_row.append(element)
                        i_have_two_values = True
                    except Exception as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element, e))
                        break

                    i_have_two_values = True
                else:
                    pass

            if i_have_two_values:
                numerical_data.append(numerical_row)
            i_have_two_values = False   
        return numerical_data

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()

def compute_daily_max_difference(time_series):
    if time_series == []:
        raise ExamException('Errore: lista valori vuota')
        
    temperature_range_list = []
    daily_measurements = 0
    index = 1
    counted = False
    single_measurement = True
    
    for i, line in enumerate(time_series):
        if i == 0 or single_measurement:
            max_temperature = line[1]
            min_temperature = line[1]
        day_start_current_epoch = line[0] - (line[0] % 86400)

        if not counted:
            for j, temporary_line in enumerate(time_series):
                day_start_temporary_epoch = temporary_line[0] - (temporary_line[0] % 86400)
                if day_start_current_epoch == day_start_temporary_epoch:

                    daily_measurements = daily_measurements + 1;
            counted = True
        if daily_measurements == 1:
            single_measurement == True

        print()
        print("Index: {}".format(index))
        print("daily_measurements: {}".format(daily_measurements))
        if index < daily_measurements and i != len(time_series) - 1:
            single_measurement = False
            if line[1] > max_temperature:
                max_temperature = line[1]
            if line[1] < min_temperature:
                min_temperature = line[1]

        else:
            if single_measurement:
                temperature_range_list.append(None)
                
            else:
                print("Current_epoch: {}".format(line[0]))
                if line[1] > max_temperature:
                    max_temperature = line[1]
                if line[1] < min_temperature:
                    min_temperature = line[1]

                range = max_temperature - min_temperature
                temperature_range_list.append(range)

                if i == len(time_series) - 1:
                    return temperature_range_list
            
                else:
                    day_start_current_epoch = line[0] - (line[0] % 86400)
                    single_measurement = True

            index = 0
            daily_measurements = 0
            counted = False

        index = index + 1

    return temperature_range_list

prova = compute_daily_max_difference(time_series) 
print(prova)