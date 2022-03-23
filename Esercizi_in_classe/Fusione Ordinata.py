lista_1 = []
x = int(input('Lista 1: Inserisci un numero intero, 0 per terminare: '))
while x != 0:
    lista_1.append(x)
    x = int(input('Lista 1: Inserisci un numero intero, 0 per terminare: '))
lista_2 = []
x = int(input('Lista 2: Inserisci un numero intero, 0 per terminare: '))
while x != 0:
    lista_2.append(x)
    x = int(input('Lista 2: Inserisci un numero intero, 0 per terminare: '))
print('Lista 1: {} Lista 2: {}'.format(lista_1,lista_2))

i, j = 0, 0; n1, n2 = len(lista_1), len(lista_2)
lista_3 = []
while i < n1 or j < n2:
    if j == n2 or i < n1 and lista_1[i] < lista_2[j]:
        lista_3.append(lista_1[i])
        i += 1
    else:
        lista_3.append(lista_2[j])
        j += 1

print('Lista 3: {}'.format(lista_3))