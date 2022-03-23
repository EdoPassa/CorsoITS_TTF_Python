lista = []
x = int(input('Inserisci un numero intero, 0 per terminare: '))
while x != 0:
    lista.append(x)
    x = int(input('Inserisci un numero intero, 0 per terminare: '))
print('Lista da sortare: {}'.format(lista))

# Seconda ottimizzazione, non ho salvato le precedenti :(
n = len(lista); i = 0; last = n-1; scambio = 0
while i < n-1 and scambio > -1:
    j = 0; scambio = -1
    while j < last:
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
            scambio = j
        j += 1
    last = scambio
    i += 1


print('Lista sortata: {}'.format(lista))