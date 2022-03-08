# Esercizio 2: leggi da tastiera il raggio di una sfera, stampa superfice e volume
from math import pi

while True:
    try:
        raggio = float(input('Inserisci raggio:'))
        superfice = 4 * pi * raggio ** 2
        volume = 4/3 * pi * raggio ** 3
        break
    except ValueError:
        print('Non è un intero riprova')


print('superfice = {}\nvolume = {}'.format(superfice,volume))

