import json

with open('json.json') as file:
    data = json.load(file)

pedidos = data['ventas']['pedidos']
pedidos_ordenados = sorted(pedidos, key=lambda x: x['fecha'], reverse=True)
print(pedidos_ordenados)