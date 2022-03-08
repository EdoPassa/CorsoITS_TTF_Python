# Esercizio 1: funzione che prende in input 2 interi e ritorna tutte le operazioni possibili tra i suddetti, i risultati
# float devono avere 2 cifre decimali

def operazioni():
    while True:
        try:
            x = int(input('x:'))
            y = int(input('y:'))
            somma = x + y
            sottrazione = x - y
            moltiplicazione = x * y
            divisione_int = x // y
            modulo = x % y
            divisione = x / y
            potenza = x ** y
            break
        except ValueError:
            print('Non è un intero riprova')
    return '\nOperazioni tra {} e {}: \n somma = {}' \
           '\n sottrazione = {}\n moltiplicazione =  {}' \
           '\n divisione_int = ' \
           '{}\n modulo = {}\n divisione = {:.2f}' \
           '\n potenza = {:.2f}'.format(x,y,somma,sottrazione,moltiplicazione,divisione_int,modulo,divisione,potenza)


print(operazioni())

