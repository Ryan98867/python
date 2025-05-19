frances =0
farofa= 0
forma=0
liso=0
integral=0
opcao=str
print ("Bem Vindo(a)! \n----PADARIA----")
print ("[1] Pão Farofa: 1,11")
print ("[2] Pão de Forma; 0,95")
print ("[3] Pão Doce Liso: 1,08")
print ("[4] Pão Frances: 1,04")
print ("[5] Pão Integral: 1,04")
print ("[6] Finalizar Compra.")
opcao=str(input("Escolha o pão desejado: "))
while opcao !="Não" and opcao != "nao" and opcao != "não" and opcao != "NAO" and opcao != "NÂO" and opcao != "Nao" and opcao != "N" and opcao != "n":
    if opcao=="1":
        print ("Você escolheu pão farofa")
        qtdfarofa=int(input("Digite a quantidade de pão farofa: "))
        farofa= qtdfarofa*1.11
        opcao= str(input("Deseja escolher outra opção? "))
    elif opcao=="2":
        print ("Você escolheu pão de forma")
        qtdforma=int(input("Digite a quantidade de pão de forma: "))
        forma = qtdforma*0.95
        opcao= str(input("Deseja escolher outra opção? "))
    elif opcao=="3":
        print ("Você escolheu pão liso")
        qtdliso=int(input("Digite a quantidade de pão liso: "))
        liso= qtdliso*1.11
        opcao= str(input("Deseja escolher outra opção? "))
    elif opcao=="4":
        print ("Você escolheu pão frances")
        qtdfrances=int(input("Digite a quantidade de pão frances: "))
        frances= qtdfrances*1.11
        opcao= str(input("Deseja escolher outra opção? "))
    elif opcao=="5":
        print ("Você escolheu pão integral")
        qtdintegral=int(input("Digite a quantidade de pão inetgral: "))
        integral= qtdintegral*1.11
        opcao= str(input("Deseja escolher outra opção? "))
    elif opcao=="Sim" or opcao== "sim" or opcao== "SIM" or opcao== "s" or opcao== "S":
        opcao=str(input("Escolha o pão desejado: "))
    
    
print ("----COMPRA----")
if farofa>0:
    print (f"Pão Farofa - quantidade{qtdfarofa} valor: {farofa:.2f} ")
if forma>0:
    print (f"Pão Farofa - quantidade{qtdforma} valor: {forma:.2f} ")
if liso>0:
    print (f"Pão Farofa - quantidade{qtdliso} valor: {liso:.2f} ")
if frances>0:
    print (f"Pão Farofa - quantidade{qtdfrances} valor: {frances:.2f} ")
if integral>0:
    print (f"Pão Farofa - quantidade{qtdintegral} valor: {integral:.2f} ")