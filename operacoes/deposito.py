def deposito(valor, saldo, extrato):
    """Realiza um depósito na conta.

    Args:
        valor (float): Valor a ser depositado.
        saldo (float): Saldo atual da conta.
        extrato (str): Extrato da conta.

    Returns:
        tuple: Novo saldo e extrato atualizado.
    """
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato