
val_base_10 = int(input('Inserisci una numero in base 10(>0): '))
base = int(input('Inserisci la nuova base(2-16): '))

if val_base_10 >= base:
    """Controllo perchè se il valore che voglio rappresentare è minore della base non serve fare operazioni"""
    x = val_base_10 // base
    resti = [val_base_10 % base]

    while x > base:
        """Algoritmo per cambiare base"""
        resti.append(x % base)
        x = x // base
    resti.append(x)

    for i in range(len(resti), 0, -1):
        """Stampo la lista al contrario, trasformando i valori > 9 in lettere maiuscole (A=65 in ASCII)"""
        if resti[i - 1] < 10:
            print(resti[i - 1], end='')
        else:
            print(chr(resti[i - 1] + ord('A') - 10), end='')

else:
    """Stampo direttamente il valore inserito"""
    if val_base_10 < 10:
        print(val_base_10)
    else:
        print(chr(val_base_10 + ord('A')-10))



