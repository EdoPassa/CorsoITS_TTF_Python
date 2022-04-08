def partizione (lista, da, a):
    p, i, j = lista[da], da, a
    while i <= j:
        if lista[i] <= p:
            i += 1
        elif lista[j] >= p:
            j -= 1
        else:
            lista[i], lista[j] = lista[j], lista[i]
    lista[da], lista[j] = lista[j], p
    return j


def quick_ric(lista, da, a):
    if da < a:
        p = partizione(lista, da, a)
        quick_ric(lista, da, p-1)
        print(lista)
        quick_ric(lista, p+1, a)
        print(lista)

lista_1 = [4,2,7,1,9,3,7,8,4,10,1,67,0,5,596]

quick_ric(lista_1, 0, len(lista_1)-1)
print(lista_1)
