import os
os.system("cls")
print("Exemplo Habilitação")
idade = int(input("Informe sua idade:"))

if idade >= 18:
    possui_carteira = input("Possui Carteira de Motorista?(1-sim 2-não)")
            
    if possui_carteira == "1":
        print("Você pode dirigir")
    else:
        print("Você não possui carteira de motorista")
else:
  print("Você não pode dirigir")