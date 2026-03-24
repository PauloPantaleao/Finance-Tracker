import json
def salvar_dados(lista):
    with open('dados.json', 'w') as data:
        json.dump(lista, data, indent= 2)
def carregar_dados():
    try:
        with open('dados.json', 'r') as data:
            return json.load(data)
    except FileNotFoundError:
        return {'salario': 0.0, 'despesas': []}
    except json.JSONDecodeError:
        return {'salario': 0.0, 'despesas': []}