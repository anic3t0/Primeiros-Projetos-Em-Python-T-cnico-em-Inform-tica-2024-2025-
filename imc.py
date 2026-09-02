peso = float(input("Digite seu peso em kg : "))

altura = float(input("Digite sua altura em metros : "))

imc = peso / (altura ** 2)

print("Sua massa corporal é :", imc)

if imc < 18.5:
    print("Você está abaixo do peso.")
elif 18.5 <= imc < 25:
    print("Seu peso está adequado.")
elif 25 <= imc < 30:
    print("Você está com sobrepeso.")
else:
    print("Você está obeso.")

