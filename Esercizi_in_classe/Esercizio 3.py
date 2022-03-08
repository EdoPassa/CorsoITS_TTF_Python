# Esercizio 3: legge da tastiera i parametri (reali) di una equazione di secondo grado

from math import sqrt

a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

delta = b ** 2 - 4 * a * c

if delta > 0:
    sol_1, sol_2 = (-b + sqrt(delta)) / 2 * a, (-b - sqrt(delta)) / 2 * a
    print("Le soluzioni sono: {} e {}".format(sol_1, sol_2))
elif delta == 0:
    sol_1_2 = -b / 2 * a
    print("La soluzione è unica ed è: {}".format(sol_1_2))
else:
    print("L'equazione non ha soluzioni reali")
