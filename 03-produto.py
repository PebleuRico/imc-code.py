import os
os.system("cls")
#Passo 01 - entrada
print("=== Bem vindo a calculadora de descomto ===")

produto =input("informe o produto:")
preco =float(input("Informe o preço"))
porcentual =float(input("informe o porcentual: "))

#Passo 02 entrada
desconto = preco * porcentual / 100
total_com_desconto = preco - desconto

#Passo 03 - saida
input("Pressione <enter> para vizualizar...")
os.system("cls")

print("=== Relatório final ===")
print("Produto:", produto)
print(f"Preço original:{produto}")
print(f"Desconto: {desconto}")
print(f"preço com desconto:{total_com_desconto}")

input("Pressione <enter> para encerrar...")