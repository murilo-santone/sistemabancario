from operacoes import deposito, sacar, extrato

def sistemaBancario():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """
    saldo = 0
    historico_extrato = ""

    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, historico_extrato = deposito.deposito(valor, saldo, historico_extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, historico_extrato = sacar.sacar(valor, saldo, historico_extrato)

        elif opcao == "e":
            extrato.extrato(saldo, historico_extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == '__main__':
    sistemaBancario()