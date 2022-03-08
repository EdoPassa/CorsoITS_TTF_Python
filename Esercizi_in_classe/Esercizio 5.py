a, b, c = int(input("primo valore: ")), int(input("secondo valore: ")), int(input("terzo valore: "))
media = (a + b + c)/3
print(f"La media è: {media}")
if a < b:
    if a < c:
        if b < c:
            print(a, b, c)
        else:
            print(a, c, b)
    else:
        print(c, a, b)
else:
    if b < c:
        if a < c:
            print(b, a, c)
        else:
            print(b, c, a)
    else:
        print(c, b, a)