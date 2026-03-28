def somar_despesas(tupla):
    total = sum(despesa[2] for despesa in tupla)
    return total
def calcular_saldo(salario, totaldespesas):
    return salario - totaldespesas