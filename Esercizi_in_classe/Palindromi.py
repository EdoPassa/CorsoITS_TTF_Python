parola = input('scrivi una parola: ')
for i in range(0, len(parola)-1):
    if parola[i] == parola[len(parola) - 1 - i]:
        palindromo = True
    else:
        palindromo = False
if palindromo:
    print('{} e palindromo'.format(parola))
else:
    print('{} non e palindromo'.format(parola))
