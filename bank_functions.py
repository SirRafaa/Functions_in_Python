contas = {}
conta_atual = None

def criar_conta():
    global conta_atual
    numero_conta = int(input("Digite o Número da conta: "))
    saldo_inicial = float(input("Digite o saldo inicial: "))
    contas[numero_conta] = saldo_inicial
    conta_atual = numero_conta
    print("Conta criada com sucesso!")

# se uma variável não possui o valor especial "None". (is Not none)
def depositar():
    global conta_atual
    if conta_atual is not None:
        valor = float(input("Digite o valor a ser depositado: "))
        contas[conta_atual] += valor
        print("Depósito realizado com sucesso!")
    else:
        print("Você precisa criar uma conta primeiro.")

def sacar():
    global conta_atual
    if conta_atual is not None:
        valor = float(input("Digite o valor a ser sacado: "))
        if contas[conta_atual] >= valor:
            contas[conta_atual] -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente.")
    else:
        print("Você precisa criar uma conta primeiro.")

def consultar_saldo():
    global conta_atual
    if conta_atual is not None:
        print(f"Saldo da conta {conta_atual}: R$ {contas[conta_atual]:.2f}")
    else:
        print("Você precisa criar uma conta primeiro.")

while True:
    print("\nMenu:")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Consultar saldo")
    print("5. Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4:
        consultar_saldo()
    elif opcao == 5:
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")