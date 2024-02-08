import json

with open('json.json') as file:
    data = json.load(file)

pedidos_valor = sorted(data['ventas']['pedidos'], key=lambda x: x['total'], reverse=True)[:2]
print(pedidos_valor)