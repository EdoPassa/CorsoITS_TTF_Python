peso, altezza = float(input("inserisci peso: ")), float(input("inserisci altezza"))
imc = peso / altezza ** 2
if imc > 40:
    print(f"L'imc è : {imc} ed sei in condizione di Obesità di III classe (gravissima)")
elif imc > 35:
    print(f"L'imc è : {imc} ed sei in condizione di Obesità di II classe (grave)")
elif imc > 30:
    print(f"L'imc è : {imc} ed sei in condizione di Obesità di I classe (moderata)")
elif imc > 25:
    print(f"L'imc è : {imc} ed sei in condizione di Sovrappeso")
elif imc > 18.5:
    print(f"L'imc è : {imc} ed sei in condizione di Regolare")
elif imc > 17.5:
    print(f"L'imc è : {imc} ed sei in condizione di Leggermente sottopeso")
elif imc > 16:
    print(f"L'imc è : {imc} ed sei in condizione di Sottopeso")
else:
    print(f"L'imc è : {imc} ed sei in condizione di Grave magrezza (inedia)")
