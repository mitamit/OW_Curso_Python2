numero = int(input("Introduce numero: "))
lista = []

while numero >= 0:
    lista.append(numero)
    numero = int(input("Introduce numero: "))

print("Máximo: %s" % max(lista))

for i in lista:
    if i % 2 == 0:
        print(i, end=" ")

print()