def extrato(saldo, extrato):
    """ Exibe o extrato bancário.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Extrato da conta.
    """
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
    print(input("Pressione Enter para sair..."))
    
