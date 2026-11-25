import os
os.system("cls")

print("Super Tabuada Com While")
numero = int(input("Informe um número:"))

contador = 0 

while contador <= 10:
    print(f"{numero} x {contador} = {numero * contador}")
    contador+=1
input("Pressione <enter> para prosseguir..")