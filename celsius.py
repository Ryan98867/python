opcao= float
print ("Escolha uma opção:")
print ("[1] Celsius para Fahrenheit: ")
print ("[2] Fahrenheit para Celsius: ")
print ("[0] Sair:")
opcao = int(input("Escolha uma opção: "))
while opcao !=0:
    if opcao==1:
        temperatura=int(input("Escolha uma temperatura:"))
        resultado= temperatura * 9 / 5 + 32
        print (f"O resultado é {resultado}")
        break
    elif opcao==2:
        temperatura=int(input("Escolha uma temperatura:"))
        resultado= temperatura + 273.15
        print (f"O resultado é {resultado}")
        break