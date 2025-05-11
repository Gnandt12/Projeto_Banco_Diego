main = """
Olá Sejam Bem Vindos Ao Banco Do Diego

Porfavor Selecione A Operação Desejada:

Tecle [1] Para Depósito
Tecle [2] Para Saque
Tecle [3] Para Visualizar Extrato
Tecle [4] Para Cancelar A Operação

=> """

saldo = 1000
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(main)

    if opcao == "1":
        valor = float(input("Insira o valor que deseja depositar: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Seu depósito foi Realizado com sucesso!Seu saldo agora é de R${saldo:.2f} ")
            

        else:
            print("Operação falhou! O valor inserido é inválido.")

    elif opcao == "2":
        valor = float(input("Insira o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! O valor inserido é insuficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor inserido excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Tentativas excedidas.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Seu Saque foi Realizado com sucesso!Seu saldo agora é de R${saldo:.2f} ")

        else:
            print("Operação falhou! O valor inserido é inválido.")

    elif opcao == "3":
        print("=======EXTRATO=======" )
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("====================")
        

    elif opcao == "4":
        print("Obrigado por utilizar o banco do Diego")
        break

    else:
        print("Operação Inválida",
              "Porfavor Tecle Uma Das Opções do Menu Abaixo")