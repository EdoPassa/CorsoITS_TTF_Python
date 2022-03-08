"""a, b = int(input("Inserisci a:")), int(input("Inserisci b:"))
i = a
mcd = 0
while i > 1 and mcd == 0:
    if a % i == 0 and b % i == 0:
        mcd = i
    else:
        i -= 1
print("mcd: {}".format(mcd))"""

# Algoritmo di Euclide
# A e B devono essere positivi e con A < B
a = int(input("Inserisci a>0:"))
while a <= 0:
    a = int(input("Inserisci a>0:"))
b = int(input("Inserisci b>0:"))
while b <= 0:
    b = int(input("Inserisci b>0:"))

if a < b:
    a, b = b, a

while  b != 0:
    resto = a % b
    a = b
    b = resto

print('MCD: {}'.format(a))
