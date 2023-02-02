class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

class IncrementModel(Model):
    def predict(self, data):
        for item in data:
            if item < 0:
                raise Exception('Numero minore di zero')
        prediction = 0
        prev_value = data[0]
        for i in range(len(data)):
            prediction = (data[i] - prev_value) + prediction
            prev_value = data[i]
        
        prediction = prediction / (len(data) - 1)
        #prediction = prediction + data[-1]
        return prediction


class FitIncrementModel(IncrementModel):
    def predict(self, data):
        for item in data:
            if item < 0:
                raise Exception('Numero minore di zero')
        prediction = 0
        prev_value = data[0]
        for i in range(len(data)):
            prediction = (data[i] - prev_value) + prediction
            prev_value = data[i]
        
        prediction = prediction / (len(data) - 1)
        
    
    def fit(self, data1, data2):
        p1 = predict(data1)
        p2 = predict(data2)
        prediction = (p1 + p2)/2
        prediction = prediction + data2[-1]
        return prediction
    
lista1 = [8, 19, 31, 41]
lista2 = [50, 52, 60]
x = FitIncrementModel()
#if not x == 65.0:
 #   raise Exception('Test non passato')
print(x.fit(lista1, lista2))

#y = Model()
#print(y.predict(lista))