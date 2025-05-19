print ("----CALCULADORA----")
print ("[1] Somar")
print ("[2] multiplicar")
print ("[3] subtrair")
print ("[4] divisao")
print ("[5] Sair")
opcao = int(input("Escolha uma opção:"))
while opcao !=5:
    if opcao ==1:
        numero1 = float(input("Escolha o primeiro numero: "))
        numero2= float(input("Escolha o segundo numero: "))
        resposta = numero1 + numero2
        print (f"{numero1} + {numero2} = {resposta}")
    elif opcao ==2:
        numero1 = float(input("Escolha o primeiro numero: "))
        numero2= float(input("Escolha o segundo numero: "))
        resposta = numero1 * numero2
        print (f"{numero1} x {numero2} = {resposta}")
    elif opcao ==3:
        numero1 = float(input("Escolha o primeiro numero: "))
        numero2= float(input("Escolha o segundo numero: "))
        resposta = numero1 - numero2
        print (f"{numero1} - {numero2} = {resposta}")
    elif opcao ==4:
        numero1 = float(input("Escolha o primeiro numero: "))
        numero2= float(input("Escolha o segundo numero: "))
        resposta = numero1 / numero2
        print (f"{numero1} / {numero2} = {resposta}")    
    

    