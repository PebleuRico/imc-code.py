import os
os.system("cls")
print(" --- LOGIN ---")
# entrada - 01
admin =input("Você é admin? (sim) (Não): ")

if admin == "sim" and admin == "nao":
   print("Proximo")

Nome_de_usuario =input("Informe o seu nome de usuario: ")
senha =input("Informe sua senha:")

if admin == "sim"  and senha == "123":
       print("Acesso liberado")
else: 
       print("Acesso Negado")
    
if Nome_de_usuario == "Gustavo lima" and senha >= 0:
 print("Acesso Liberado")
