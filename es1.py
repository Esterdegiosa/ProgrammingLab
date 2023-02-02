class ExamException(Exception):
        pass

class MovingAverage():
    def __init__(self, finestra):
        self.finestra = finestra
        
    def compute(self, data, finestra):
        if data == []:
            raise ExamException('Errore: lista valori vuota')
        if type(finestra) is not int:
            raise ExamException('Errore: finestra non intera')
        if finestra <= 0:
            raise ExamException('Errore: finestra non positiva')
        if finestra > len(data):
            raise ExamException('Errore: finestra maggiore del numero dei valori')

        for item in data:
            if type(item) is str or type(item) is bool or type(item) is None:
                raise ExamException('Errore: i valori devono essere numerici')
            
        average_list = []
        for i in range(len(data) - finestra + 1):
            tot = 0
            for j in range(i, finestra + i):
                tot = tot + data[j]
            media = tot/finestra
            average_list.append(media)
        return average_list

#moving_average = MovingAverage(2)
#result = moving_average.compute([2, 4, 8, 16])
#print(result)