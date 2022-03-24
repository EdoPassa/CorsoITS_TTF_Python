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

'''n = int(input('Inserisci la dimensione n: '))
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
    print()'''

# Esercizio 3

def lettura_matrice(nome, n=None, m=None):
    if n is None:
       n = int(input('Inserisci la dimensione n: '))
    if m is None:
        m = int(input('Inserisci la dimensione m: '))
    matrice = []
    for i in range(0, n):
        lista_t = []
        for j in range(0, m):
            lista_t.append(int(input(f'{nome} {i}:{j}: ')))
        matrice.append(lista_t)
    return matrice


def prodotto_matriciale(m_1, m_2):
    if righe(m_1) == colonne(m_2):
        m_prodotto = []
        for i in range(0, righe(m_1)):
            m_prodotto.append([])
            for j in range(0, colonne(m_2)):
                m_prodotto[i].append(0)
                for k in range(0, righe(m_2)):
                    m_prodotto[i][j] += m_1[i][k]*m_2[k][j]
        return m_prodotto
    else:
        print('Le righe della prima matrice devono essere uguali alle colonne della seconda')


def stampa_matrice(m, nome=None):
    if nome:
        print(nome)
    for i in range(0, righe(m)):
        for j in range(0, colonne(m)):
            print(m[i][j], end='\t')
        print()


def righe(matrice):
    return len(matrice)


def colonne(matrice):
    return  len(matrice[0])


#matrice_1 = lettura_matrice('Matrice 1'); matrice_2 = lettura_matrice('Matrice 2')
#prodotto_1_2 = prodotto_matriciale(matrice_1,matrice_2)
#stampa_matrice(prodotto_1_2, 'Prodotto')
