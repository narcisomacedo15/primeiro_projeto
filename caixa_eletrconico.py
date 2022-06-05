print('*' * 30)
print('|' + ' ' * 7 + 'BANCO DE TODOS' + ' ' * 7 + '|')
print('|' + ' ' * 7 + 'Saque 24 Horas' + ' ' * 7 + '|')
print('*' * 30)
print('Seja bem vindo!')

print('1 - Depósito')
print('2 - Saque')
print('3 - Consulta Saldo')
print('0 - Encerrar')
opcao = int(input('Digite a opção desejada: '))

deposito = 0
saque = 0
saldo_conta = 0

while opcao != 0:

    if opcao == 1:
        deposito = float(input('Digite o valor desejado: '))
        deposito = deposito
        print('Depósito realizado com sucesso!')
        nova_operacao = input('Deseja realizar nova oepração? Digite "S - Sim" ou "N - Não": ')
        if nova_operacao == 'S':
            opcao = int(input('Digite a opção desejada: '))
        else:
            print('Encerrando seção...')
            break

    elif opcao == 2:
        saque = saque
        saque = float(input('Digite o valor desejado: '))
        print('Saque realizado com sucesso!')
        nova_operacao = input('Deseja realizar nova oepração? Digite "S - Sim" ou "N - Não": ')
        if nova_operacao == 'S':
            opcao = int(input('Digite a opção desejada: '))
        else:
            print('Encerrando seção...')
            break

    elif opcao == 3:
        saldo_conta = deposito - saque
        print('Saldo em conta é: {}.'.format(saldo_conta))
        nova_operacao = input('Deseja realizar nova oepração? Digite "S - Sim" ou "N - Não": ')
        if nova_operacao == 'S':
            opcao = int(input('Digite a opção desejada: '))
        else:
            print('Encerrando seção...')
            break

print('Volte sempre!')