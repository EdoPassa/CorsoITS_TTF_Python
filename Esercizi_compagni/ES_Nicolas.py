import math
import timeit

start = timeit.default_timer()
def primo(y, n):
    d = 0
    z = 2
    q = int(math.sqrt(y))
    if q == 2:
        q += 1
    while z <= q and d == 0:
        if y % z == 0:
            d = 1
        z += 1
        n += 1
    if d == 0:
        return y, n
    else:
        return 0, n


x = int(input('inserisci numero '))
c = 0
divprim = []
div = []
f=0
for i in range(2, int(math.sqrt(x))+1):
    f += 1
    l, f = primo(i, f)
    if l != 0:
        divprim.append(l)
i = 0
while i < len(divprim):
    if x % divprim[i] == 0:
        c = 1
        div.append(divprim[i])
        p, f = primo(x//divprim[i], f)
        if p != 0 and p != divprim[i]:
            div.append(x//divprim[i])
    i += 1
    f += 1
print(f'numero finale di cicli = {f}')
if c == 1:
    print('il numero non è primo')
    print(f'divisori primi: {div}')
else:
    print('il numero è primo')

stop = timeit.default_timer()

print('Time: ', stop - start)