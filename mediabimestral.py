b1 = int(input("Insira sua nota do primeiro bimestre:"))
pv = int(input("Insira sua nota do segundo bimestre:"))
tb = int(input("Insira nota do trabalho:"))
b2 = (pv + tb) / 2
Mb = (b1 + b2)

if Mb >= 7:
    print("aprovado")
else:
    print("reprovado")