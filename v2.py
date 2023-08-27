import textwrap

def menu():
    menu = """\n
    ##### MENU #####
    [d]\tDeposito
    [s]\tSaque
    [e]\tExtrato
    [lu]\tListar Usuários
    [lc]\tListar Contas
    [cu]\tCadastrar Usuário
    [cc]\tCadastrar Conta
    [q]\Sair
    =>"""
    return input(textwrap.dedent(menu))


#def menu_operacao():
    menu_operacao = """\n
    ##### OPERACOES #####
    [
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_operacao))    


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("\n!!! Valor inválido !!!")
    
    return saldo, extrato


def sacar(*, saldo, valor, extrato, saques, limite):
    
    if valor > saldo:
        print("\n!!! Saldo insuficiente !!!")
    elif valor > limite:
        print("\n!!! Limite de saque excedido !!!")

    else:
        saldo -= valor
        extrato += f"\nSaque: R$ {valor:.2f}\n"
        saques += valor
    
    return saldo, extrato, saques

def retirar_extrato(saldo,/, *,extrato):
    print("\n ###### EXTRATO ######")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}\n")
    print("\n ###### FIM EXTRATO ######")

def cadastrar_usuario(usuarios):
    print("\n###### CADASTRAR USUÁRIO ######")
    cpf = input("\nDigite o CPF do usuário: ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("\n !!! Usuário já cadastrado com esse CPF !!!")
        return
    
    nome = input("\nDigite o nome completo: ")
    data_nascimento = input("\nDigite a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nDigite o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\n!!! Usuário cadastrado com sucesso !!!")

def filtrar_usuario(usuarios, cpf):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    print("\n###### CRIAR CONTA ######")
    cpf = input("\nDigite o CPF do usuário: ")
    usuario = filtrar_usuario(usuarios, cpf)

    if usuario:
        print("\n!!! Conta criada com sucesso !!!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("\n!!! Usuário não encontrado !!!")

def filtrar_conta(contas, cpf):
    conta_filtrada = [conta for conta in contas if conta["usuario"]["cpf"] == cpf]
    return conta_filtrada[0] if conta_filtrada else None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\n
        Agência: \t{conta["agencia"]}
        C/C: \t{conta["numero_conta"]}
        Titular: \t{conta["usuario"]["nome"]}
        """
        print("#"*100)
        print(textwrap.dedent(linha))

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""\n
        Nome: \t{usuario["nome"]}
        CPF: \t{usuario["cpf"]}
        Data de Nascimento: \t{usuario["data_nascimento"]}
        Endereço: \t{usuario["endereco"]}
        """
        print("#"*100)
        print(textwrap.dedent(linha))

def entrar_conta(contas, usuarios):
    print("\n###### ENTRAR NA CONTA ######")
    cpf = input("\nDigite o CPF do usuário: ")
    usuario = filtrar_usuario(usuarios, cpf)
    conta = filtrar_conta(contas, cpf)
    return conta

def main():
    LIMITE_SAQUES = 1500
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            print("\n###### DEPÓSITO ######")
            valor = float(input("\nDigite o valor do depósito: "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "s":
            if saldo == 0:
                print("\n!!! Saldo ins  uficiente !!!")
                print("\n!!! Faça um depósito antes de sacar !!!")
            elif saques >= LIMITE_SAQUES:
                print("\n!!! Limite diário de saques excedido !!!")
            else:
                print("\n###### SAQUE ######")
                valor = float(input("\nDigite o valor do saque: "))
                saldo, extrato, saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                saques=saques, 
                limite=limite)

        elif opcao == "e":
            retirar_extrato(saldo, extrato=extrato)


        elif opcao == "lu":
            print("\n###### LISTAR USUÁRIOS ######")
            listar_usuarios(usuarios)

        elif opcao == "lc":
            print("\n###### LISTAR CONTAS ######")
            listar_contas(contas)

        elif opcao == "cu":
            cadastrar_usuario(usuarios)

        elif opcao == "cc":
            conta = criar_conta(AGENCIA, len(contas)+1, usuarios)
            if conta:
                contas.append(conta)

        elif opcao == "q":
            print("\n###### SAIR ######")
            print("\n!!! Saindo do sistema !!!")
            break

        else:
            print("\n!!! Opção inválida !!!")

main()