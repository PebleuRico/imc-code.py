import os 
os.system("cls")

#Começo
print("=== ESTACIONAMENTO ===") 
print("Olá, você ligou para == ESTAPAR ESTACIONAMENTOS ==") 
print("\nVamos realizar a sua cobrança")
print("Opção 1: Cobrança")
print("Opção 2: Desligar")

nome = input("Com quem estou falando?: ")
opcao = input("Escolha uma opção: ")

print("Olá senhor(a)", nome)

# Opções
if opcao == "2":
    print("O que achou desta ligação?")
    print("Digite de 1 a 5: ")
    nota = int(input("Qual a sua nota?: "))

    if 1 <= nota <= 5:
        print("OBRIGADO(A)!!")
        print("Sua Nota foi", nota)
        print("Ligação encerrada")
# Veículos
elif opcao == "1":
    print(nome, "qual é o seu veículo?")
    print("--- VEÍCULOS ---")
    print("1 - MOTO - R$ 5,00 POR HORA")
    print("2 - CARRO - R$ 8,00 POR HORA")
    print("3 - SUV - R$ 12,00 POR HORA")
    
    veiculo = input("Digite o número das opções de veículo: ")

    if veiculo == "1":
        nome_veiculo = "Moto"
        valor_hora = 5
    elif veiculo == "2":
        nome_veiculo = "Carro"
        valor_hora = 8
    elif veiculo == "3":
        nome_veiculo = "SUV"
        valor_hora = 12
    else:
        print("Veículo Inválido!")
        valor_hora = 0
       # Calculos  
    if valor_hora > 0:
        horas = float(input("Quantas horas ficou estacionado? "))

      
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
    
     # FINALIZAÇÃO
        print("Vimos aqui e essas são as cobranças:")
        print("===== RESUMO DA COBRANÇA =====")
        print("Cliente:", nome)
        print("Veículo:", nome_veiculo)
        print("Horas estacionado:", horas)
        print("Valor da permanência: R$", valor_permanencia)
        print("Taxa adicional: R$", taxa)
        print("Valor total: R$", valor_total)
        print("Valor médio por hora: R$", valor_medio)
             

            #SAÍDA 2.5 (LIGAÇÂO ENCERRADA)
        print("\nligação encerrada")
        print("\nO que achou desta ligação?")
        nota = int(input("Qual a sua nota de 1 a 5?: "))
        if 1 <= nota <= 5:
            print("\nOBRIGADO(A)!!")
            print("Sua Nota foi", nota)