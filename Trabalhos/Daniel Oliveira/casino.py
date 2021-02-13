import random
import os

def limpa_ecra():
    os.system("cls")

def cabecalho(texto):
    limpa_ecra()
    print("="*20)
    print(texto)
    print("="*20)

def add_dinheiro():
    cabecalho("  Introduzir Saldo")

    money = float(input("\nIntroduza uma Quantia de Dinheiro: "))
    moedas = money * 100
    dinheiro.append(moedas)
    moedas = sum(dinheiro)
    dinheiro [0] = moedas
    print("Introduziu", money, "$ e ficou com um total de",moedas,"Moedas para apostar!\n")
    print("Boa Sorte!!!")
    input("Carrega ENTER p/ continuar... ")


def ver_dinheiro():
    cabecalho("     Ver Saldo")

    moedas = dinheiro[0]
    print("\nVocê tem", moedas, "Moedas para apostar!")
    money = moedas / 100
    print("O que corresponde a", money,"$\n")
    print("Boa Sorte!!!")
    input("Carrega ENTER p/ continuar... ")

def rem_dinheiro():
    cabecalho("   Levantar Saldo")

    levantar = 0
    moedas = dinheiro[0]
    money = moedas / 100

    print("\nVocê tem", money, "$")
    levantar = float(input("Quanto dinheiro quer levantar: "))
    
    if levantar <= money:
        money = money - levantar
        moedas = money * 100
        dinheiro [0] = moedas
        print("\nVocê levantou", levantar,"$")
    else:
        print("\nDinheiro insuficiente\n")
    
    input("Carrega ENTER p/ continuar... ")

def slotmachine():
    cabecalho("    SlotMachine")

    symbols = ["@","#","$","&"]

    moedas = dinheiro[0]
    print("Bem Vindo à SlotMachine\n")
    while moedas > 0:
        print("Você tem", moedas, "Moedas para Apostar")
        try:
            aposta = float(input("Quanto quer Apostar: "))
        except:
            print("\nEntre com uma quantia de dinheiro")
            continue
        if aposta > moedas:
            print("\nDinheiro insuficiente\n")
            continue
        else:
            moedas -= aposta
            simb_um = random.choice(symbols)
            simb_dois = random.choice(symbols)
            simb_tres = random.choice(symbols)

            print()

            print("="*13)
            print("|", random.choice(symbols),"|", random.choice(symbols),"|", random.choice(symbols),"|")
            print("="*13)

            print("|",simb_um,"|",simb_dois,"|",simb_tres,"|   <------")
            print("="*13)

            print("|", random.choice(symbols),"|", random.choice(symbols),"|", random.choice(symbols),"|")
            print("="*13)

            if simb_um == simb_dois == simb_tres:
                quantia = aposta*2
                print("\nParabéns Ganhas-Te ", quantia, " Moedas")
                moedas += quantia
            else:
                print("\nPerdeu!!!")
            break
    dinheiro[0] = moedas
    print("Obrigado Por Jogares")
    input("Carrega ENTER p/ continuar... ")

def blackjack():
    cabecalho("     BlackJack")

    dealer_cartas = []
    jogador_cartas = []

    moedas = dinheiro[0]
    print("Bem Vindo ao BlackJack\n")
    while moedas > 0:
        print("Você tem", moedas, "Moedas para apostar")
        try:
            aposta = float(input("Quanto quer Apostar: "))
        except:
            print("\nEntre com uma quantia de dinheiro")
            continue
        if aposta > moedas:
            print("\nDinheiro insuficiente\n")
            continue
        else:
            moedas -= aposta

            dealer_cartas.append(random.randint(1, 11))
            print("\nO Dealer tem: " + str(sum(dealer_cartas)))

            while len(jogador_cartas) != 2:
                jogador_cartas.append(random.randint(1, 11))
                if len(jogador_cartas) == 2:
                    print("Tu tens " + str(sum(jogador_cartas)) + " com as cartas", jogador_cartas)

            while sum(jogador_cartas) < 21:
                apostar = str(input("Queres apostar ou manter ? "))
                if apostar == "apostar":
                    jogador_cartas.append(random.randint(1, 11))
                    print("\nTens um total de " + str(sum(jogador_cartas)) + " com as cartas", jogador_cartas)
                else:
                    while sum(dealer_cartas) < 17:
                        dealer_cartas.append(random.randint(1, 11))

                    if sum(dealer_cartas) == 21:
                        print("\nO Dealer tem um total de " + str(sum(dealer_cartas)) + " com", dealer_cartas)
                        print("O Dealer fez 21!!! O Dealer Ganhou!\n")
                        break
                    elif sum(dealer_cartas) > 21:
                        print("\nO Dealer tem um total de " + str(sum(dealer_cartas)) + " com", dealer_cartas)
                        print("O Dealer rebentou!")
                        quantia = aposta*2
                        print("\nParabéns Ganhas-te ", quantia, " Moedas")
                        moedas += quantia
                        break
                    print("\nO Dealer tem um total de " + str(sum(dealer_cartas)) + " com", dealer_cartas)
                    print("Tens um total de " + str(sum(jogador_cartas)) + " com", jogador_cartas)
                    if sum(dealer_cartas) >= sum(jogador_cartas):
                        print("\nO Dealer Ganhou!\n")
                        break
                    else:
                        print("\nGANHAS-TE!")
                        quantia = aposta*2
                        print("Parabéns Ganhas-te ", quantia, " Moedas\n")
                        moedas += quantia
                        break

            if sum(jogador_cartas) > 21:
                print("\nREBENTAS-TE! O Dealer ganhou.\n")
            elif sum(jogador_cartas) == 21:
                print("\nFizes-te BLACKJACK! GANHAS-TE!!!")
                quantia = aposta*2
                print("Parabéns Ganhas-te", quantia, "Moedas\n")
                moedas += quantia
            break
    dinheiro[0] = moedas
    print("Obrigado Por Jogares")
    input("Carrega ENTER p/ continuar... ")

def maior_menor():
    cabecalho("     Maior ou Menor")

    chave = []

    moedas = dinheiro[0]

    print("Bem Vindo ao Maior ou Menor\n")
    print("Adivinha o Número de 1 a 50")
    print("Com apenas 5 tentativas\n")

    chave.append(random.randint(1, 51))
    adivinha = 0
    contador =  1
    i = 0 

    while moedas > 0:
        print("Tu tens", moedas, "Moedas para apostar")
        try:
            aposta = float(input("Quantia da Aposta: "))
        except:
            print("\nEntre com uma quantia de dinheiro")
            continue
        if aposta > moedas:
            print("\nDinheiro insuficiente\n")
            continue
        else:
            moedas -= aposta

            for i in range(1,6):
                print("\nTentativa nº", contador)
                adivinha = int(input (""))
                if adivinha == sum(chave):
                    print("GANHAS-TE!!!")
                    quantia = aposta*2
                    print("\nParabéns Ganhas-te ", quantia, " Moedas")
                    moedas += quantia
                    break
                else:
                    if adivinha > sum(chave):
                        print("O Número é Mais Baixo")
                    else:
                        print("O Número é Mais Alto")
                if i == 5:
                    print("\nPerdeu!")
                    print("O Número era", sum(chave),"\n")
                contador = contador + 1
        break
    dinheiro[0] = moedas
    print("Obrigado Por Jogares")
    input("Carrega ENTER p/ continuar... ")

def main():

    global dinheiro
    dinheiro = []

    while True:
        cabecalho("-------CA$INO-------")

        print("1. Introduzir Saldo")
        print("2. Ver Saldo")
        print("3. Levantar Saldo")  
        print("4. Slot Machine")
        print("5. BlackJack")
        print("6. Maior ou Menor")
        print("7. Sair")
        print("="*20)
        print()

        opcao = int(input("Escolha uma Opção: "))

        if opcao == 1:
            add_dinheiro()
        elif opcao == 2:
            ver_dinheiro()
        elif opcao == 3:
            rem_dinheiro()    
        elif opcao == 4:
            slotmachine()
        elif opcao == 5:
            blackjack()
        elif opcao == 6:
             maior_menor()
        elif opcao == 7:
            print("\nAté à Próxima!\n")
            input("")
            break
        else:
            print("Opção Errada!")
            input("Carrega ENTER p/ continuar... ")

if __name__ == "__main__":
    main()