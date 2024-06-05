            ###Simulador Bancário###

from datetime import datetime

def mostrar_menu():
    return """
[1] Deposito
[2] Sacar
[3] Extrato
[4] Sair

=> """

def deposito(saldo, extrato):
    valor = float(input("Digite o valor do depósito: \n"))
    if valor > 0:
        saldo += valor
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"{data_hora} - Depósito: R$ {valor:.2f} \n"
        print("Depósito realizado com sucesso!")
    else:
        print("Falha na operação! O valor informado é inválido.")
    return saldo, extrato

def saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: \n"))
    saldo_excedido = valor > saldo
    excedeu_limite = valor > limite
    saque_do_dia_excedido = numero_saques >= LIMITE_SAQUES
    if saldo_excedido:
        print("Falha na operação! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Falha na operação! O valor do saque excedeu o limite.")
    elif saque_do_dia_excedido:
        print("Falha na operação! Número de saques diários excedido.")
    elif valor > 0:
        saldo -= valor
        data_hora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        extrato += f"{data_hora} - Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("A operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=========================================")

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:
        opcao = input(mostrar_menu())
        if opcao == "1":
            saldo, extrato = deposito(saldo, extrato)
        elif opcao == "2":
            saldo, extrato, numero_saques = saque(saldo, extrato, numero_saques, limite, LIMITE_SAQUES)
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
        elif opcao == "4":
            break
        else:
            print("Operação inválida, por favor selecione novamente a opção desejada.")

if __name__ == "__main__":
    main()
