import os
os.system("cls")

#Criando uma lista ou array em python
nomes = ["Caio", "Roberval", "José"]
#           0         1         2    => indice
indice = 0
#Exibindo o item da posição 2 da lista
print(f"O Nome da posição 0: {nomes[indice]}")
print(f"O Nome da posição 1: {nomes[1]}")
print(f"O Nome da posição 2: {nomes[2]}")

print("=======================================")
#Exibindo a Lista toda
print(nomes)

input("Pressione enter para finalizar...")

#Alterando um elemento da lista
nomes[1] = "Maria"
print(f"Lista de nomes atualizadas: {nomes}")


input("Pressione Enter para finalizar...")

#Adicionar um elemento na lista (append | insert)
os.system("cls")
nome = input("Digite um nome:")
nomes.append(nome)
print(f"Lista de nomes atualizada: {nomes}")

input("Pressione Enter para finalizar...")
nomes.insert(0, "Carolina")
print(f"Lista de nomes atualizadas: {nomes}")

#Excluindo um elemento da lista (pop e o del)
input("Pressione Enter para finalzar...")
del nomes[3]
print(f"Lista de nomes atualizadas: {nomes}")

nome_excluido = nomes.pop(1)
print(f"O nome {nome_excluido} Foi removido com sucesso da lista!")
print(f"Lista de nomes atualzada: {nomes}")

input("Pressione Enter para Finalizar...")

#Apaga os elementos da lista
nomes.clear()
print(f"Lista de Nomes atualizada: {nomes}")

#Exemplo de dicionário
cliente = {
    "nome": "Caio",
    "cpf": "123.123.321-32",
    "email":"md,caio@yahoo.gmail.com.br",
    "idade": 32
}

print(f"O CPF do cliente é: {cliente["cpf"]}")