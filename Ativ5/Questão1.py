from estruturas_dados import Fila

fila_impressao = Fila()
print(f"Fila de impressão inicial: {fila_impressao}")

print("\n--- Inserindo documentos ---")
fila_impressao.enfileirar("Documento A.pdf")
print(f"Após enfileirar 'Documento A.pdf': {fila_impressao}")
fila_impressao.enfileirar("Relatório Mensal.docx")
print(f"Após enfileirar 'Relatório Mensal.docx': {fila_impressao}")
fila_impressao.enfileirar("Imagem_001.png")
print(f"Após enfileirar 'Imagem_001.png': {fila_impressao}")

print("\n--- Verificando situações da fila ---")
print(f"Primeiro documento na fila: {fila_impressao.primeiro()}")
print(f"Último documento na fila: {fila_impressao.ultimo()}")
print(f"Quantidade de documentos na fila: {fila_impressao.tamanho()}")

print("\n--- Simulando impressão ---")
documento_impresso = fila_impressao.desenfileirar()
print(f"Documento impresso: {documento_impresso}. Fila atual: {fila_impressao}")
print(f"Primeiro documento na fila agora: {fila_impressao.primeiro()}")
print(f"Quantidade de documentos na fila agora: {fila_impressao.tamanho()}")

documento_impresso = fila_impressao.desenfileirar()
print(f"Documento impresso: {documento_impresso}. Fila atual: {fila_impressao}")
print(f"Quantidade de documentos na fila agora: {fila_impressao.tamanho()}")

print("\n--- Verificando fila vazia ---")
print(f"A fila está vazia? {fila_impressao.esta_vazia()}")
fila_impressao.desenfileirar() # Tentando desenfileirar de uma fila com um item
fila_impressao.desenfileirar() # Tentando desenfileirar de uma fila vazia
print(f"Fila após tentar desenfileirar mais: {fila_impressao}")
print(f"A fila está vazia? {fila_impressao.esta_vazia()}")
