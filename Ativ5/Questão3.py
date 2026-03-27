from estruturas_dados import Fila

fila_pedidos = Fila()
print(f"Fila de pedidos inicial: {fila_pedidos}")

print("\n--- Inserindo pedidos ---")
fila_pedidos.enfileirar("Pedido 1 (Pizza Calabresa)")
print(f"Após enfileirar 'Pedido 1 (Pizza Calabresa)': {fila_pedidos}")
fila_pedidos.enfileirar("Pedido 2 (Lasanha)")
print(f"Após enfileirar 'Pedido 2 (Lasanha)': {fila_pedidos}")
fila_pedidos.enfileirar("Pedido 3 (Refrigerante)")
print(f"Após enfileirar 'Pedido 3 (Refrigerante)': {fila_pedidos}")

print("\n--- Verificando situações da fila ---")
print(f"Primeiro pedido na fila: {fila_pedidos.primeiro()}")
print(f"Último pedido na fila: {fila_pedidos.ultimo()}")
print(f"Quantidade de pedidos na fila: {fila_pedidos.tamanho()}")


