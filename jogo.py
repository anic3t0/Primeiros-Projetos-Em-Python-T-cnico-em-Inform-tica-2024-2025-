print("Bem vindo ao jogo! O computador escolheu uma palavra aleatória e você deve adivinhar qual é, fique tranquilo que ao longo do jogo você receberá dicas para ajudá-lo")
print('A palavra pode ser um:')

opções = ["objeto", "nome", "animal", "ou local"]
for opção in opções:
    print(opção)
    
print("E o jogo tem três dificuldades:")
dificuldades = ["facil", "medio", "dificil"]
for escolha in dificuldades:
    print(escolha)
dificuldade = input("Escolha a dificuldade:")

# Modo fácil
if dificuldade == "facil":
    palavra_secreta = 'pato'
    dicas = ('tem pernas', 'gosta de nadar', 'faz quack')
    print('Você tem 10 tentativas, a primeira dica é: é branco')
    tentativas = 10
    indice_dica = 0

    while tentativas > 0:
        resposta = input("Insira sua resposta:")
    
        if resposta.lower() == palavra_secreta:
            print('Você adivinhou, parabéns')
            break
        else:
            tentativas -= 1
            print('Resposta incorreta, tente novamente. Tentativas restantes:', tentativas)
        
            if indice_dica < len(dicas):
                print("Dica:", dicas[indice_dica])
                indice_dica += 1
           
            if tentativas == 0:
                print('Você perdeu, a resposta era:', palavra_secreta)
                
# Modo médio
elif dificuldade == "medio":
    palavra_secreta = 'Cristo Redentor'
    dicas = ('inaugurado em 1931', 'fica localizado no topo de um morro', 'feito de concreto armado')
    print('Você tem 10 tentativas, a primeira dica é: tem 30 metros de altura')
    tentativas = 10
    indice_dica = 0

    while tentativas > 0:
        resposta = input("Insira sua resposta:")
    
        if resposta.lower() == palavra_secreta.lower():
            print('Você adivinhou, parabéns')
            break
        else:
            tentativas -= 1
            print('Resposta incorreta, tente novamente. Tentativas restantes:', tentativas)
        
            if indice_dica < len(dicas):
                print("Dica:", dicas[indice_dica])
                indice_dica += 1
          
            if tentativas == 0:
                print('Você perdeu, a resposta era:', palavra_secreta)
                
# Modo difícil               
elif dificuldade == "dificil":
    palavra_secreta = 'Alan Turing'
    dicas = ('desenvolveu o conceito de máquina universal', 'nasceu em 1912 e morreu em 1954', 'pioneiro na ciência da computação')
    print('Você tem 10 tentativas, a primeira dica é: figura importante')
    tentativas = 10
    indice_dica = 0

    while tentativas > 0:
        resposta = input("Insira sua resposta:")
        
        if resposta.lower() == palavra_secreta.lower():
            print('Você adivinhou, parabéns')
            break
        else:
            tentativas -= 1
            print('Resposta incorreta, tente novamente. Tentativas restantes:', tentativas)
        
            if indice_dica < len(dicas):
                print("Dica:", dicas[indice_dica])
                indice_dica += 1
          
            if tentativas == 0:
                print('Você perdeu, a resposta era:', palavra_secreta)
else:
    print("Opção inválida, por favor escolha fácil, médio ou difícil")