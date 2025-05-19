print ("CALCULO IMC")
nome= str(input("Qual é o seu nome? "))
idade= int(input("Qual e sua idade? "))
peso= float(input("QUal o seu peso? "))
altura= float(input("Qual a sua altura? "))
imc= peso/(altura*altura)
if imc<18.5:
    print ("Classificação: Abaixo do peso")
elif  imc > 18.5 and imc<24.9:
    print ("Classificação: Peso Normal")
elif imc >24.9 and imc <30:
    print ("Classificação: Sobrepeso")
elif imc>30:
    print ("Classificação: Obesidade")