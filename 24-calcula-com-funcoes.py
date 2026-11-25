import funcoes

funcoes.limpar_telas()


#Definindo as minhas funções
def limpar_tela():
    funcoes.system("cls")

def somar(n1, n2):
    total = n1 + n2
    print(f"a soma é: {total}")

def subtrair(n1,n2):
    total = n1 - n2
    return total

def multiplicar(n1,n2):
    total = n1 * n2
    return total

def dividir(n1,n2):
    total = n1 / n2
    return total

def imprimir_erros():
    print("Operador Invalido")

print("Seja Bem vindo a calculadora com Funções")
n1 = int(input("informe o primeiro numero:"))
n2 = int(input("informe o segundo numero:"))

limpar_tela()

print("==Escolha uma operação==")
print("[1] - somar")
print("[2] - Subtrair")
print("[3] - Multiplicar")
print("[4] - Dividir")
opcao = int(input("Escola uma opção: "))

limpar_tela()

if(opcao == 1):
    #somar
    somar(n1,n2)

elif(opcao == 2):
    #Subtrair
  print(f"A subtração será:{subtrair(n1,n2)}")

elif(opcao == 3):
    #Multiplicar
    print(f"A multiplicação será:{multiplicar(n1,n2)}")

elif(opcao == 4):
    #Dividir
    print(f"A divisão será:{dividir(n1,n2)}")
else:
    #Exiba uma mensagem de erro

    imprimir_erros()