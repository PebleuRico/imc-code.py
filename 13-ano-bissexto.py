import os
os.system("cls")

Ano = int(input("Digite o ANO: "))
if Ano % 4 == 0: 
    print("Ano Bissexto")
else:
    print("Não é um ano bissexto")
