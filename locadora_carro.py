print ("-----locadora-----")
print ("Valores dos carros")
print ("1 - Jeta")
print("2 - BMW 320i")
print("3 - Corolla")
print("4 finalizar locação")
print("0 - Sair")
opcao = int(input("escolha uma opção: "))
while opcao !=0:
    if opcao ==1:
        print("Carro escolhido jetta")
        print("Valor diario: 100,00")
        print("Valor por km: 1,00")
        opcao= int(input("escolha outra opção: "))
    elif opcao ==2:
        print("Carro escolhido bmw 320i")
        print("Valor diario: 130,00")
        print("Valor por km: 1,80")
        opcao= int(input("escolha outra opção: "))
    elif opcao ==3:
        print("Carro escolhido Corolla")
        print("Valor diario: 110,00")
        print("Valor por km: 1,20")
        opcao= int(input("escolha outra opção: "))
    elif opcao==4:
        print("1 - jetta")
        print("2 - bmw320i")
        print("3 - corolla")
        opcaocarro= int(input("Qual o carro escolhido?"))
        if opcaocarro ==1:
            print("Voce escolheu jetta")
            diasalugados= int(input("Quantos dias alugados: "))
            kmpercorrido= float(input("Km percorrido: "))
            total= (kmpercorrido * 1.00) + (diasalugados * 100)
            print(f"o total e de {total}")
            break
        elif opcaocarro ==2:
            print("Voce escolheu BMW 320i")
            diasalugados= int(input("Quantos dias alugados: "))
            kmpercorrido= float(input("Km percorrido: "))
            total= (kmpercorrido * 1.80) + (diasalugados * 130)
            print(f"o total e de {total}")
            break
        elif opcaocarro ==3:
            print("Voce escolheu corolla")
            diasalugados= int(input("Quantos dias alugados: "))
            kmpercorrido= float(input("Km percorrido: "))
            total= (kmpercorrido * 1.20) + (diasalugados * 110)
            print(f"o total e de {total}")
            break
        
        
        