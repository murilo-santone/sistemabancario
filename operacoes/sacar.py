def sacar(valor, saldo, extrato):
    """Realiza o saque de um valor da conta, atualizando o saldo e o extrato.
        Args:
        valor (float): Valor a ser sacado.
        saldo (float): Saldo atual da conta.
        extrato (str): Extrato da conta.

    Returns:
        tuple: Novo saldo e extrato atualizado.
    """
    numero_saques = 0
    LIMITE_SAQUES = 3
    limite = 500
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    
    return saldo, extrato