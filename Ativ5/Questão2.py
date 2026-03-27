from estruturas_dados import Fila

fila_banco = Fila()
print(f"Fila de atendimento inicial: {fila_banco}")

print("\n--- Inserindo clientes ---")
fila_banco.enfileirar("Cliente 1 (João)")
print(f"Após enfileirar 'Cliente 1 (João)': {fila_banco}")
fila_banco.enfileirar("Cliente 2 (Maria)")
print(f"Após enfileirar 'Cliente 2 (Maria)': {fila_banco}")
fila_banco.enfileirar("Cliente 3 (Pedro)")
print(f"Após enfileirar 'Cliente 3 (Pedro)': {fila_banco}")

print("\n--- Verificando situações da fila ---")
print(f"Primeiro cliente na fila: {fila_banco.primeiro()}")
print(f"Último cliente na fila: {fila_banco.ultimo()}")
print(f"Quantidade de clientes na fila: {fila_banco.tamanho()}")

print("\n--- Simulando atendimento ---")
cliente_atendido = fila_banco.desenfileirar()
print(f"Cliente atendido: {cliente_atendido}. Fila atual: {fila_banco}")
print(f"Primeiro cliente na fila agora: {fila_banco.primeiro()}")
print(f"Quantidade de clientes na fila agora: {fila_banco.tamanho()}")

cliente_atendido = fila_banco.desenfileirar()
print(f"Cliente atendido: {cliente_atendido}. Fila atual: {fila_banco}")
print(f"Quantidade de clientes na fila agora: {fila_banco.tamanho()}")

print("\n--- Verificando fila vazia ---")
print(f"A fila está vazia? {fila_banco.esta_vazia()}")
fila_banco.desenfileirar() # Tentando desenfileirar de uma fila com um item
fila_banco.desenfileirar() # Tentando desenfileirar de uma fila vazia
print(f"Fila após tentar desenfileirar mais: {fila_banco}")
print(f"A fila está vazia? {fila_banco.esta_vazia()}")
