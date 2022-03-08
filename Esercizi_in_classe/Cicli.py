x = int(input("inserisci in numero( > 0 per terminare): "))

while x > 0:
    prime_check = 0
    for i in range(1, x + 1 ):
        if x % i == 0:
            prime_check += 1
    if prime_check == 2:
        print("è primo")
    else:
        print("non è primo")
    x = int(input("inserisci in numero(negativo o 0 per terminare): "))
