from estruturas_dados import Fila

fila_impressao = Fila()
print(f"Fila de impressão inicial: {fila_impressao}")

fila_impressao.enfileirar("Documento A.pdf")
print(f"Após enfileirar 'Documento A.pdf': {fila_impressao}")
fila_impressao.enfileirar("Relatório Mensal.docx")
print(f"Após enfileirar 'Relatório Mensal.docx': {fila_impressao}")
fila_impressao.enfileirar("Imagem_001.png")
print(f"Após enfileirar 'Imagem_001.png': {fila_impressao}")

print(f"Primeiro documento na fila: {fila_impressao.primeiro()}")
print(f"Último documento na fila: {fila_impressao.ultimo()}")
print(f"Quantidade de documentos na fila: {fila_impressao.tamanho()}")
