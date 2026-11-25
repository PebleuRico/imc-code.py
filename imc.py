import os
os.system("cls")

print("=== CALCULADORA DE IMC ===")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

