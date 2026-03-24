def adicionar_despesa(lista, descricao, valor):
    despesa = {'descricao': descricao, 'valor': float(valor)}
    lista['despesas'].append(despesa)
def remover_despesa(lista, indice):
    lista['despesas'].pop(indice)
def mudar_salario(lista, salario):
    lista['salario'] = salario
def somar_despesas(lista):
    total = sum(despesa['valor'] for despesa in lista)
    return total
def calcular_saldo(salario, totaldespesas):
    return salario - totaldespesas