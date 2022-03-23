# Esercizio 1

"""n = int(input('Inserisci la dimensione n: '))
M = []
for i in range(0, n):
    lista_t = []
    for j in range(0, n):
       lista_t.append(int(input(f'{i}:{j}: ')))
    M.append(lista_t)

for i in range(0, n):
    for j in range(0, n):
        print(M[i][j], end='\t')
    print()"""

# Esercizio 2

n = int(input('Inserisci la dimensione n: '))
M_1 = []
for i in range(0, n):
    lista_t = []
    for j in range(0, n):
       lista_t.append(int(input(f'M1{i}:{j}: ')))
    M_1.append(lista_t)
M_2 = []
for i in range(0, n):
    lista_t = []
    for j in range(0, n):
       lista_t.append(int(input(f'M2{i}:{j}: ')))
    M_2.append(lista_t)

M_Prodotto = []
for i in range(0, n):
    lista_t = []
    for j in range(0, n):
        prodotto = 0
        for k in range(0, n):
            prodotto += M_1[i][k]*M_2[k][j]
        lista_t.append(prodotto)
    M_Prodotto.append(lista_t)

for i in range(0, n):
    for j in range(0, n):
        print(M_Prodotto[i][j], end='\t')
    print()
