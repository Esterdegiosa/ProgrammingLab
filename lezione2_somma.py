#Funziona
def sum_list(list):
    sum = 0
    if list == []:
        return None
        
    for item in list:
        sum = sum + item
    return sum

list = []
x = sum_list(list)
print(x)