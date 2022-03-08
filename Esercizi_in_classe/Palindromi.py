parola = input('scrivi una parola: ')
palindromo = True
count = 0
for i in range(0, len(parola)//2):
    count += 1
    if parola[i] != parola[len(parola) - 1 - i]:
        palindromo = False


print('è palindromo'if palindromo else 'non è palindromo')
print(count)
