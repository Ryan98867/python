salario =0
comicao = 0.15
meta = 0
total = 0
tsalario = 0
nome = str

nome = (input("Escreva seu nome: "))
salario = float(input("digite seu salario: "))
meta = int(input("Quantas vendas voce fez? "))

total = salario*comicao
tsalario = total+salario

if meta >20:
    print("voce bateu sua meta!!")
    print(f"seu salario e de {tsalario} ")
    
else:
    print("Voce não bateu sua meta")
    print(f"seu salario e de {salario}")