lista = []
x = int(input('Inserischi un numero intero, 0 per terminare: '))
while x != 0:
    lista.append(x)
    x = int(input('Inserischi un numero intero, 0 per terminare: '))
print('Lista da sortare: {}'.format(lista))

n = len(lista)
for i in range(1, n):
    j = i - 1
    while j >= 0 and lista[j+1] < lista[j]:
        popped_x = lista.pop(j+1)
        lista.insert(j, popped_x)
        j -= 1

print('Lista sortata: {}'.format(lista))

