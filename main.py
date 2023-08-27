def depositar(saldo,valor,extrato, /):
    print("Depósito")
       
    saldo += valor
    extrato += f"Depósito: R${valor}\n"
    print("\n Depósito realizado com sucesso! ")

    return saldo, extrato

def sacar(*,saldo,valor,extrato, limite, numero_saques, saques):
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
        numero_saques += 1
        print("Saque realizado com sucesso")
    
    return saldo, extrato

def exibir_extrato(saldo,/,*,extrato):
    print("Extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R${saldo}")

def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf,usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n Usuário criado com sucesso! ")

def filtrar_usuario(cpf,usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("Usuário não encontrado")
    
menu = """
[d]\tDeposito
[s]\tSaque
[e]\tExtrato
[q]\tSair
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
saques = 0
usuarios = []
contas = []
LIMITE_SAQUES = 1500
AGENCIA = "0001"

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Digite o valor do depósito: "))
        if valor >0: 
            saldo, extrato = depositar(saldo,valor,extrato)
        else:
            print("Valor inválido")

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
            saldo, saques, numero_saques, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato, limite=limite, numero_saques=numero_saques, saques=saques)
    
    elif opcao == "e":
        print("Extrato")
        print(extrato)
        print(f"Saldo: R${saldo}")
    
    elif opcao == "nu":
            criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)

        if conta:
            contas.append(conta)


    elif opcao == "q":
        break

    else:
        print("Opção inválida")
