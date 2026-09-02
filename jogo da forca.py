import random

palavras = ['banana', 'abacaxi', 'morango', 'laranja', 'uva']
palavra = random.choice(palavras)
letras_adivinhadas = []
tentativas_maximas = 6

while True:

    palavra_parcial = ''.join(letra if letra in letras_adivinhadas else '' for letra in palavra)
    print("Palavra:", palavra_parcial)

    if palavra_parcial == palavra:
        print("Parabéns! Você acertou a palavra:", palavra)
        break

    letra = input("Digite uma letra: ").lower()

    if letra in letras_adivinhadas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    letras_adivinhadas.append(letra)

    if letra not in palavra:
        print("A letra", letra, "não está na palavra.")
        tentativas_maximas -= 1
        print("Você tem", tentativas_maximas, "tentativas restantes.")
        if tentativas_maximas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break
