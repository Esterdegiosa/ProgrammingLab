my_file = open("shampoo_sales.csv", "r")
for line in my_file:
    elements = line.split(",")

for line in my_file:
    print(line)