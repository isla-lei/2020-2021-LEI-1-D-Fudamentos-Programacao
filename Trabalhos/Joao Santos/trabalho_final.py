import os

def limpa_ecra():
    os.system("cls")


#pedra papel tesoura



def jogo_pedra():
    import time
    import random
    computador  = ["pedra", "papel", "tesoura"]
    
    

    while True:
        print("-=" * 20)
        print("jogo pedra, papel e tesoura")
        print("-=" * 20)
        print("[0] pedra")
        print("[1] tesoura")
        print("[2] papel")
        print()
        
        jogador = int(input("escolha um elemento: "))
        if jogador >=3 or jogador <=-1:
            print("número errado")
            jogo_pedra()
    
        print("pedra")
        time.sleep(0.8)
        print("papel")
        time.sleep(0.8)
        print("tesoura!!!!!!")
        time.sleep(0.8)
        print()
    
        c = random.choice(computador)
    
        print("-=" * 20)
        print("O computador escolheu:",c)
        print("-=" * 20)
    
        if jogador == 0:
            print("O jogador escolheu: pedra")
        elif jogador == 1:
            print("O jogador escolheu: tesoura ")
        else:
            print("O jogador escolheu: papel")
        
        print("-=" * 20)

    
        if c == "pedra":
            if jogador == 0:
                print()
                time.sleep(0.8)
                print("Empate")

            elif jogador == 1:
                print()
                time.sleep(0.8)
                print("O computador ganhou ")

            else:
                print()
                time.sleep(0.8)
                print("O jogador ganhou")

    
        elif  c == "papel":
            if jogador == 0:
                print()
                time.sleep(0.8)
                print("O computador ganhou")
            elif jogador == 1:
                print()
                time.sleep(0.8)
                print("O jogador ganhou")
  
            else:
                time.sleep(0.8)
                print()
                print("Empate")
    
        elif c == "tesoura":
            if jogador == 0:
                time.sleep(0.8)
                print()
                print("O jogador ganhou")
            elif jogador == 1:
                time.sleep(0.8)
                print()
                print("empate")
            else:
                time.sleep(0.8)
                print()
                print("O computador ganhou")
            
        
        time.sleep(0.5)

        print()

        a = input("S/para continuar ou n/para terminar: ")
        if a == "s":
            limpa_ecra()
            jogo_pedra()
        else:
            limpa_ecra()
            main()


def jogo_adivinha():
    from random import randint
    import time
    

    computador = randint(1, 50)
    
    print("-" * 20 )
    print("O jogo da adivinha")
    print("-" * 20 )

    tentativas = 0

    while True:
        jogador = int(input("Qual é o valor em que eu estou a pensar entre(1, 50): "))
        tentativas = tentativas + 1
        if jogador <0.5 or jogador > 51:
            print("numero invalido ")
            jogo_adivinha()
        if jogador > computador:
            time.sleep(0.5)
            print("O meu valor é mais baixo")
            print()
        elif jogador < computador:
            time.sleep(0.5)
            print("O meu valor é mais alto")
            print()
        else:
            time.sleep(0.5)
            print("Parabens você acertou")
            print()
            print("O nº de tentativas: ",tentativas)
            break
    
    if jogador == computador:
        print()
        b =input("s/para continuar ou n/para terminar ")
        if b == "s" or b == "S" :
            limpa_ecra()
            jogo_adivinha()
        else:
            limpa_ecra()
            main()


def cabecalho(texto):
    print("="*25)
    print(texto)
    print("="*25)

import sys

def main():


    while True:
        cabecalho("MENU")

        print(" 1. jogo da pedra, papel, tesoura")
        print(" 2. jogo da adivinha")
        print(" 3. Sair")
        

        print()
        opcao = int(input(" Escolha opcão: "))

        if opcao == 1:
            limpa_ecra()
            jogo_pedra()
        elif opcao ==2:
            limpa_ecra()
            jogo_adivinha()
        elif opcao ==3:
            sys.exit()
        else:
            print("opção errada!")

if __name__ == "__main__":
    main()