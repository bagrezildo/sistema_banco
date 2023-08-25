menu = """
[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
saques = 0
LIMITE_SAQUES = 1500

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor do depósito: "))
        saldo += valor
        extrato += f"Depósito: R${valor}\n"

    elif opcao == "s":
        print("Saque")
        if saldo == 0:
            print("Saldo insuficiente")
            print("Faça um depósito antes de sacar")
            continue
        valor = float(input("Digite o valor do saque: "))
        if valor > saldo:
            print("Saldo insuficiente")
        elif valor > limite:
            print("Limite de saque excedido")
        elif saques > LIMITE_SAQUES:
            print("Limite diário de saques excedido!")
        else:
            saldo -= valor
            saques += valor
            extrato += f"Saque: R${valor}\n"
            print("Saque realizado com sucesso")
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo: R${saldo}")

    elif opcao == "q":
        break

    else:
        print("Opção inválida")
