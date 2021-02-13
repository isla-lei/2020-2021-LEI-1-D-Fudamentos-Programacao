import random
import os
os.system('cls')


def menu():
    print("=======ADIVINHA O NÚMERO======")
    input("Pressione ENTER para continuar")

    os.system('cls')
    print('\n' * 80)

    print("="*24)
    print("**********MENU**********")
    print("="*24)


    continuar = 1
    while continuar:
        continuar = int(input("1. Jogar \n" +
                              "0. Sair\n"))

        os.system('cls')
        print('\n' * 80)

        if continuar:
            game()
        else:
            print("Saindo...")


def game():
    erros = 0
    sorteado = random.randrange(0, 100)
    jogador = int(input("Digite um numero: "))
    while (sorteado != jogador):
        os.system('cls')
        if (sorteado > jogador):
            print("--> ###ERRO### \n" +
                  "O NUMERO E MAIOR")
        elif (sorteado < jogador):
            print("--> ###ERRO### \n" +
                  "O NUMERO E MENOR")
        erros += 1
        jogador = int(input("Digite um numero: "))
    print("Numero " + str(jogador) + ", voce acertou em " + str(erros + 1) + " tentativas")
    print("@@@@@@-PARABÉNS-@@@@@@")


menu()
