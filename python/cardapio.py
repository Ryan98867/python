opcao = 0
while opcao !=5:
    print("Cardapio")
    print("1- Hamburguer")
    print("2- pizza")
    print("3- Salada")
    print("4- Refrigerante")
    print("5- Sair")
    opcao = int(input("escolha uma opção: "))
    
    if opcao == 1: 
        print("Voce escolheu hHamburguer")
    elif opcao ==2:
        print("Voce escolheru pizza")
    elif opcao ==3:
        print("Voce escolheu salada")
    elif opcao ==4:
        print("Voce escolheu refrigerante")
    elif opcao ==5:
        print("Saindo do cardapio...")
        break
    else:
        print("opção invalida. Tente novamente") 