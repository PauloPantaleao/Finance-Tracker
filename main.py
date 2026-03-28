import operacoes
import write
import banco
from time import sleep
banco.inicializar_banco()
while True:
    write.line()
    write.title('GERENCIADOR FINANCEIRO')
    write.line()
    despesas = banco.get_despesas()
    salario = banco.get_salario()
    total = operacoes.somar_despesas(despesas)
    sleep(1)
    print(f'{'Salário:':<24}R${salario:>14.2f}')
    print(f'{'Despesas:':<24}R${total:>14.2f}')
    print(f'{'Saldo:':<24}R${operacoes.calcular_saldo(salario, total):>14.2f}')
    write.line()
    ordem = 1
    for despesa in despesas:
        print(f'{ordem}.', end='')
        print(f'{despesa[1]:^18}', end='')
        print(f'[id:{despesa[0]}]', end='  ')
        print(f'R$  {despesa[2]:>8.2f}')
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
        banco.adicionar_despesas(desc, val)
        write.line()
        write.title('Adicionando Despesa...')
        sleep(1)
    elif escolha == 'R':
        indice = int(input('Digite o id da despesa: '))
        banco.remover_despesa(indice)
        write.line()
        write.title('Removendo Despesa...')
        sleep(1)
    elif escolha == 'S':
        novo = float(input('Digite o novo salário: '))
        banco.set_salario(novo)
        write.line()
        write.title('Modificando salário...')
        sleep(1)
    elif escolha == 'X':
        write.title('Encerrando aplicação...')
        sleep(1)
        break
    else:
        print('Erro.')
write.line()
write.title('ATÉ A PROXIMA!')
write.line()
