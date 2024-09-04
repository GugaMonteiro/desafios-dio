print('================ Seja Bem Vindo ao Novo Sistema Bancário ================')
print('\nEscolha uma opção abaixo:')

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(deposito):
    if deposito > 0:
        global saldo
        global extrato
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        print('Depósito realizado com sucesso!')
    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar():
    global saldo
    global extrato
    global numero_saques
    saldo -= valor
    extrato += f"Saque: R$ {valor:.2f}\n"
    numero_saques += 1
    print('-' * 42)
    print('Saque realizado com sucesso!')


while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            sacar()

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("="*42)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")