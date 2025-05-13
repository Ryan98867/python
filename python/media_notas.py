media= float
nota1 = float(input("digite a nota do seu trabalho: "))
nota2 = float(input("Dogite a nota da sua prova: "))
media = (nota2+nota1)/2

print (f"a media de sua nota e de {media}")

if media >=7:
    print("Voce foi aprovado")

else:
    print("voce foi reporvado")