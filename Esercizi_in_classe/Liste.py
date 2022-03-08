x = int(input("inserisci un numero intero, 0 per terminare: "))
lista = []
while x != 0:
    lista.append(x)
    x = int(input("inserisci un numero intero, 0 per terminare: "))
for i in range(len(lista), 0, -1):
    print(lista[i-1])
