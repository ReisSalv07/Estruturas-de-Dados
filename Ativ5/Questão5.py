from estruturas_dados import Fila

fila_pedidos_online = Fila()
print(f"Fila de pedidos online inicial: {fila_pedidos_online}")

print("\n--- Inserindo pedidos online ---")
fila_pedidos_online.enfileirar("Pedido #1001 (Smartphone)")
print(f"Após enfileirar \'Pedido #1001 (Smartphone)\': {fila_pedidos_online}")
fila_pedidos_online.enfileirar("Pedido #1002 (Smartwatch)")
print(f"Após enfileirar \'Pedido #1002 (Smartwatch)\': {fila_pedidos_online}")
fila_pedidos_online.enfileirar("Pedido #1003 (Fone de ouvido)")
print(f"Após enfileirar \'Pedido #1003 (Fone de ouvido)\': {fila_pedidos_online}")

print("\n--- Verificando situações da fila ---")
print(f"Primeiro pedido na fila: {fila_pedidos_online.primeiro()}")
print(f"Último pedido na fila: {fila_pedidos_online.ultimo()}")
print(f"Quantidade de pedidos na fila: {fila_pedidos_online.tamanho()}")

print("\n--- Processando pedidos online ---")
pedido_processado = fila_pedidos_online.desenfileirar()
print(f"Pedido processado: {pedido_processado}. Fila atual: {fila_pedidos_online}")
print(f"Primeiro pedido na fila agora: {fila_pedidos_online.primeiro()}")
print(f"Quantidade de pedidos na fila agora: {fila_pedidos_online.tamanho()}")

pedido_processado = fila_pedidos_online.desenfileirar()
print(f"Pedido processado: {pedido_processado}. Fila atual: {fila_pedidos_online}")
print(f"Quantidade de pedidos na fila agora: {fila_pedidos_online.tamanho()}")

print("\n--- Verificando fila vazia ---")
print(f"A fila está vazia? {fila_pedidos_online.esta_vazia()}")
fila_pedidos_online.desenfileirar() # Processando o último pedido
print(f"Fila após processar o último pedido: {fila_pedidos_online}")
print(f"A fila está vazia? {fila_pedidos_online.esta_vazia()}")
