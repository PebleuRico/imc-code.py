import os
os.system("cls")
ano_atual = int(input("Informe o ano atual:"))
idade_atual = int(input("Informe sua idade: "))
ano_futuro =  int(input("Informe o ano futuro: "))

anos_que_faltam = ano_futuro - ano_atual

idade_futura = idade_atual + anos_que_faltam
print("idade futura é:" "{idade_futura}")
