lista = []
x = int(input('Inserischi un numero intero, 0 per terminare: '))
while x != 0:
    lista.append(x)
    x = int(input('Inserischi un numero intero, 0 per terminare: '))
print('Lista da sortare: {}'.format(lista))

n = len(lista)
sort = False
for j in range(0, n-1):
    if not sort:
        sort = True
        for i in range(0, n-1-j):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                sort = False
        print('Ciclo {}: {}'.format(j, lista))
    else:
        break

print('Lista sortata: {}'.format(lista))