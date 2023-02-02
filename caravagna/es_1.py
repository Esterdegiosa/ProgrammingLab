def somma_vettoriale(lista1, lista2):
    for item in lista1:
        if type(item) is int:
            return []

    for item in lista2:
        if type(item) != int:
            return []
    
    if len(lista1) != len(lista2):
        return []

    sum = 0
    for i in range((len(lista1))):
        x = lista1[i] * lista2[i]
        sum = sum + x

    return sum


lista1 = [3, 1, 2]
lista2 = [1, 2, 1.2]
y = somma_vettoriale(lista1, lista2)
print(y)