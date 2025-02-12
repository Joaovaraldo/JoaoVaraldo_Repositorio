import random

def jogar():
    opcoes = ["Pedra", "Papel", "Tesoura"]
    
    # Solicitar escolha do jogador
    escolha_jogador = input("Escolha 0 para Pedra, 1 para Papel ou 2 para Tesoura: ")
    
    # Validar a entrada
    if escolha_jogador not in ['0', '1', '2']:
        print("Opção inválida")
        return
    
    escolha_jogador = int(escolha_jogador)
    escolha_computador = random.randint(0, 2)
    
    print(f"Você escolheu: {opcoes[escolha_jogador]}")
    print(f"O computador escolheu: {opcoes[escolha_computador]}")
    
    # Determinar o vencedor
    if escolha_jogador == escolha_computador:
        print("Empate!")
    elif (escolha_jogador == 0 and escolha_computador == 2) or \
         (escolha_jogador == 1 and escolha_computador == 0) or \
         (escolha_jogador == 2 and escolha_computador == 1):
        print("Você venceu!")
    else:
        print("O computador venceu!")
    
    # Perguntar se o jogador quer jogar novamente
    jogar_novamente = input("Vamos jogar novamente? (Sim/Não): ").strip().lower()
    
    if jogar_novamente == 'sim':
        jogar()
    else:
        print("Jogo encerrado. Até a próxima!")

# Iniciar o jogo
jogar()