import os
os.system ("cls")

print("SIstema Boletim")

nome = input("informe o nome do aluno:")
nota1 = float(input("Informe a primeira nota:"))
nota2 = float(input("Informe a segunda nota:"))
nota3 = float(input("informe a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >=7:
    print("Parabéns! Você foi aprovado!")

elif media >=4 and media <7:
    print("Opsss, Você está de recuperação")
else: 
    print("Não foi dessa vez, você reprovou")
