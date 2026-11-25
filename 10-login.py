import os
os.system("cls")

usuario = input("Informe sua senha de usuario:")
senha = input("Informe sua senha de usuario:")
if usuario == "admin" and senha == "123":
    print("Acesso Liberado")
else:
    print("Acesso negado")