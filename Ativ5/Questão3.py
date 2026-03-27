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

print("\n--- Simulando processamento de pedidos ---")
pedido_processado = fila_pedidos.desenfileirar()
print(f"Pedido processado: {pedido_processado}. Fila atual: {fila_pedidos}")
print(f"Primeiro pedido na fila agora: {fila_pedidos.primeiro()}")
print(f"Quantidade de pedidos na fila agora: {fila_pedidos.tamanho()}")

pedido_processado = fila_pedidos.desenfileirar()
print(f"Pedido processado: {pedido_processado}. Fila atual: {fila_pedidos}")
print(f"Quantidade de pedidos na fila agora: {fila_pedidos.tamanho()}")

print("\n--- Verificando fila vazia ---")
print(f"A fila está vazia? {fila_pedidos.esta_vazia()}")
fila_pedidos.desenfileirar() # Tentando desenfileirar de uma fila com um item
fila_pedidos.desenfileirar() # Tentando desenfileirar de uma fila vazia
print(f"Fila após tentar desenfileirar mais: {fila_pedidos}")
print(f"A fila está vazia? {fila_pedidos.esta_vazia()}")
