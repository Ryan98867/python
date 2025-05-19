import random
numero_secreto = random.randint (1,100000)
tentativas = 0
contagem_tentativas = 0
print("-------Jogo da adivinhação------")
print("Tente adivinhar o numero secreto")
while tentativas != numero_secreto:
    numero =int(input("Digite um numero de 1 a 10:"))
    contagem_tentativas = contagem_tentativas+1
    
    if numero == numero_secreto:
        print("Parabens!!! Voce acertou")
        print(f"Voce precisou de {contagem_tentativas}")
        break
    elif numero < numero_secreto:
        print("O numero secreto e maior")
        
        
    else:
        print("O numero secreto e menor.")
       
