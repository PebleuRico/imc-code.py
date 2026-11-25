import os
os.system("cls")
print("---- CONSUMO MÉDIO DE LITROS ---")

#Entrada - 01 Fome

km =float(input("informe a quantidade de quilometros:"))
litros =float(input("informe a quantidade de litros:"))

consumo = km / litros 
print(f"consumo médio:{consumo}")