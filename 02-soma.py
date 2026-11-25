import os 
os.system("cls")

print("Programa da soma")

resposta = "sim"

while resposta == "sim":

     numero1 = int(input("Digite um numero: "))
     numero2 = int(input("Digite outro numero: "))
     total = numero1 + numero2 
     print(f"A soma será: {total}")

     resposta = input("Digite Sim para executar Novamente: ")

     os.system("cls")
     
input("Pressione <enter> para sair..")
