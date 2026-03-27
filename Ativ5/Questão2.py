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
