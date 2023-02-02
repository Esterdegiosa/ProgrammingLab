#Funziona
class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        
        for item in data:
            if item < 0:
                raise Exception('Non è possibile aver un numero minore di zero')
        
        prediction = 0
        prev_value = data[0]
        for i in range(len(data)):
            prediction = (data[i] - prev_value) + prediction
            prev_value = data[i]
        
        prediction = prediction / (len(data) - 1)
        prediction = prediction + data[-1]
        return prediction

lista = [50, 52, 60]
x = IncrementModel()
#if not x == 65.0:
 #   raise Exception('Test non passato')
print(x.predict(lista))