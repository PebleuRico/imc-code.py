import os 
os.system("cls")

print("=== ESTACIONAMENTO ===") 

print("OLá, você ligou para ESTAPAR Estacionamentos")
print("Vamos realizar a sua cobrança")
print("Opção 1: Cobrança")
print("Opção 2: Desligar ")

nome = input("Com quem estou falando?:  ")
opcao = input("Escolha uma opção: ")

print("Olá senhor(a)", nome)

# Entrada 01 - Menu

# Opções       

#OPÇÂO 2 SAÍDA
if opcao == "2":
    print("Oque achou desta ligação")
    print("Digite de 1 a 5: ")

    nota = int(input("Qual a sua nota?: "))

    if nota >= 1 and nota <= 5:
        print("OBRIGADO(A)!!")
        print("Sua Nota foi", nota)
        print("ligação encerrada")

#OPÇÂO 1 COBRANÇA

#VEICULOS
elif opcao =="1":
    print(f"{nome}, Qual é o seu veiculo?")
    print("--- VEICULOS ---")
    print("1 - MOTO - R$ 5,00 POR HORA ")
    print ("2 - CARRO - R$ 8,00 POR HORA")
    print("3 - SUV - R$ 12,00 POR HORA")

    veiculo = input("Digite o numero nas opções de veiculo: ")
# PREÇO DA MOTO
    if veiculo == "1":
        nome_veiculo = "Moto"
        valor_hora = 5

#PREÇO DO CARRO
    elif veiculo == "2":
        nome_veiculo = "Carro"
        valor_hora = 8

#PREÇO DO SUV
    elif veiculo == "3":
        nome_veiculo = "SUV"
        valor_hora = 12
    else:
        print("Veiculo Invalido")
 
# HORAS
    bome_veiculo = "Desconhecido"
    valor_hora = 0

if valor_hora > 0:
    horas = float(input("Quantas horas ficou estacionado? "))
          
 # Calculo
    valor_permanencia = valor_hora * horas
 
 # Calcular a taxa adicional
    if horas > 10:
        taxa = valor_permanencia * 0.10
  
    elif horas > 5:
        taxa = valor_permanencia * 0.05
 
    else:
        taxa = 0
 
# Calcula o valor total e média
        valor_total = valor_permanencia + taxa
        valor_medio = valor_total / horas if horas > 0 else 0 
 
# MOSTRA TODAS AS INFORMAÇÕES FINAIS
        print("Vimos aqui e essas são as cobranças")
        print("===== RESUMO DA COBRANÇA =====")
        print("Cliente:", nome)
        print("Veículo:", nome_veiculo)
        print("Horas estacionado:", horas)
        print("Valor da permanência: R$", valor_permanencia)
        print("Taxa adicional: R$", taxa)
        print("Valor total:", valor_total)
        print("Valor médio por hora: R$", valor_medio)
          
 #SAÍDA 2.5 (LIGAÇÂO ENCERRADA)
    enter = input("Digite < 2 > para desligar:  ")
    if enter == "2":
           print("Essa foi sua cobrança!")
           print("Oque achou desta ligação")
           print("Digite de 1 a 5: ")

    nota = int(input("Qual a sua nota?: "))
    if nota >= 1 and nota <= 5:
           print("OBRIGADO(A)!!")
           print("Sua Nota foi", nota)
           print("ligação encerrada")