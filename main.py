import func
import operacoes
import write
from time import sleep
dados = func.carregar_dados()
while True:
    write.line()
    write.title('GERENCIADOR FINANCEIRO')
    write.line()
    despesas = dados['despesas']
    total = operacoes.somar_despesas(despesas)
    sleep(1)
    print(f'{'Salário:':<17}R${dados['salario']:>11.2f}')
    print(f'{'Despesas:':<17}R${total:>11.2f}')
    print(f'{'Saldo:':<17}R${operacoes.calcular_saldo(dados['salario'], total):>11.2f}')
    write.line()
    ordem = 1
    for despesa in despesas:
        print(f'{ordem}.', end='')
        print(f'{despesa['descricao']:^15}', end='')
        print(f'R$ {despesa['valor']:>10.2f}')
        ordem += 1
    write.line()
    print('[A] Adicionar  [R] Remover  [S] Salário  [X] Sair')
    write.line()
    escolha = ''
    while escolha not in ['A', 'R', 'S', 'X']:
        escolha = str(input()[0]).upper()
    sleep(0.5)
    write.line()
    if escolha == 'A':
        desc = str(input('Descrição: '))
        val = float(input('Valor: '))
        operacoes.adicionar_despesa(dados, desc, val)
        write.line()
        write.title('Adicionando Despesa...')
        sleep(1)
        func.salvar_dados(dados)
    elif escolha == 'R':
        indice = int(input('Digite o índice: ')) - 1
        operacoes.remover_despesa(dados, indice)
        write.line()
        write.title('Removendo Despesa...')
        sleep(1)
        func.salvar_dados(dados)
    elif escolha == 'S':
        novo = float(input('Digite o novo salário: '))
        operacoes.mudar_salario(dados, novo)
        write.line()
        write.title('Modificando salário...')
        sleep(1)
        func.salvar_dados(dados)
    elif escolha == 'X':
        func.salvar_dados(dados)
        write.title('Encerrando aplicação...')
        sleep(1)
        break
    else:
        print('Erro.')
write.line()
write.title('ATÉ A PROXIMA!')
write.line()
