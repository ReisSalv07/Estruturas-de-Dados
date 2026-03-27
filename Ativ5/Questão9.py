from estruturas_dados import Pilha

def identificar_operadores(expressao):
    pilha_operadores = Pilha()
    operadores_validos = {
        '+': 'Adição',
        '-': 'Subtração',
        '*': 'Multiplicação',
        '/': 'Divisão',
        '^': 'Exponenciação',
        '(': 'Parêntese de Abertura',
        ')': 'Parêntese de Fechamento'
    }
    
    operadores_encontrados = set() # Usar um set para garantir operadores únicos

    print(f"Analisando a expressão: {expressao}")
    for char in expressao:
        if char in operadores_validos:
            pilha_operadores.empilhar(char)
            operadores_encontrados.add(char)

    print("Operadores únicos encontrados na expressão:")
    for op in sorted(list(operadores_encontrados)): # Ordena para uma saída consistente
        print(f"- {op} ({operadores_validos[op]})")

    print("\nConteúdo final da pilha (após empilhar todos os operadores):", pilha_operadores)
