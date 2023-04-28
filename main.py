menu = """
Informe o número da operação que deseja fazer:

1 - Depositar
2 - Sacar
3 - Extrato
0 - Sair

Sua escolha: """
saldo = 0.0
limite_valor_saque = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print('Bem vindo ao sistema bancário!')

while True:
    opcao = input(menu)

    if opcao == '1':
        print('Área de depósito')
        valor_deposito = float(input('Informe o valor a ser depositado: R$ '))
        
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'DEPÓSITO..........+R$ {valor_deposito:.2f}\n'
            print(f'Valor de R$ {valor_deposito:.2f} depositado com sucesso!')

        else:
            print(f'Valor informado é igual ou menor que 0 e é inválido.')

    elif opcao == '2':
        print('Área de Saque')

        if numero_saques >= LIMITE_SAQUES:
            print('Você atingiu o número máximo de 3 saques diários.')
            continue

        valor_saque = float(input('Informe o valor a ser sacado: R$ '))
        
        if valor_saque > 500:
            print('Valor excede o limite.\nO limite para cada saque é R$ 500,00.')

        elif valor_saque > 0 and valor_saque <= saldo:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f'SAQUE.............-R$ {valor_saque:.2f}\n'
            print(f'Valor de R$ {valor_saque:.2f} sacado com sucesso!')

        elif valor_saque > saldo:
            print('Saldo insuficiente para saque.')

        else:
            print('Valor informado é igual ou menos que 0 e é inválido.')

    elif opcao == '3':
        print('EXTRATO BANCÁRIO\n')
        print(extrato)
        print(f'SALDO.............R$ {saldo:.2f}')
        
    elif opcao == '0':
        break

    else:
        print('Opção inválida')

print('Até logo!')