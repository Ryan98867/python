frances =0
farofa= 0
forma=0
liso=0
integral=0
opcao=0
print ("Bem Vindo(a)! \n----PADARIA----")
print ("[1] Pão Farofa: 1,11")
print ("[2] Pão de Forma; 0,95")
print ("[3] Pão Doce Liso: 1,08")
print ("[4] Pão Frances: 1,04")
print ("[5] Pão Integral: 1,04")
print ("[6] Finalizar Compra.")
opcao=int(input("Escolha o pão desejado: "))
while opcao !=6:
    if opcao==1:
        print ("Você escolheu pão farofa")
        qtdfarofa=int(input("Digite a quantidade de pão farofa: "))
        farofa= qtdfarofa*1.11
        opcao= int(input("escolha outra opção: "))
    elif opcao==2:
        print ("Você escolheu pão de forma")
        qtdforma=int(input("Digite a quantidade de pão de forma: "))
        forma = qtdforma*0.95
        opcao= int(input("escolha outra opção: "))
    elif opcao==3:
        print ("Você escolheu pão liso")
        qtdliso=int(input("Digite a quantidade de pão liso: "))
        liso= qtdliso*1.11
        opcao= int(input("escolha outra opção: "))
    elif opcao==4:
        print ("Você escolheu pão frances")
        qtdfrances=int(input("Digite a quantidade de pão frances: "))
        frances= qtdfrances*1.11
        opcao= int(input("escolha outra opção: "))
    elif opcao==5:
        print ("Você escolheu pão integral")
        qtdintegral=int(input("Digite a quantidade de pão inetgral: "))
        integral= qtdintegral*1.11
        opcao= int(input("escolha outra opção: "))
 
print ("----COMPRA----")
if farofa>0:
    print (f"Pão Farofa - quantidade{qtdfarofa} valor: {farofa}")
if forma>0:
    print (f"Pão Forma - quantidade{qtdforma} valor: {forma}")
if liso>0:
    print (f"Pão Doce Liso - quantidade{qtdliso} valor: {liso}")
if frances>0:
    print (f"Pão Frances - quantidade{qtdfrances} valor: {frances} ")
if integral>0:
    print (f"Pão Integral- quantidade{qtdintegral} valor: {integral}")
    
elif escolha in cardapio:("Pão de forma: ")
 total + =cardapio[escolha]
 print(f"escolha)adicionada.") Total atual:R${total:2f}")
else:
print ("Produto nao encontrado no cardapio.")
    
print (f"\nTotal da compra:R${total:2f}")
pagamento=float(input("Digite o valor pago:R$"))
if pagamento>=total:
    troco=pagamneto-total
    print(f"Pagamento aceito.Troco:R${troco:2f}")
    print ("Obrigado pela preferência!")
else:
    print ("Pagamento insuficiente.Tente novamente")