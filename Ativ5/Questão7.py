from estruturas_dados import Pilha

def calculadora_rpn(expressao):
    pilha = Pilha()
    operadores = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '/': lambda a, b: a / b,
        '^': lambda a, b: a ** b
    }

    tokens = expressao.split()

    for token in tokens:
        if token not in operadores:
            try:
                pilha.empilhar(float(token))
            except ValueError:
                return f"Erro: Token inválido \'{token}\'"
        else:
            if pilha.tamanho() < 2:
                return "Erro: Expressão RPN inválida - poucos operandos para o operador " + token
            operando2 = pilha.desempilhar()
            operando1 = pilha.desempilhar()

            if token == '/' and operando2 == 0:
                return "Erro: Divisão por zero"
            
            resultado = operadores[token](operando1, operando2)
            pilha.empilhar(resultado)

    if pilha.tamanho() == 1:
        return pilha.desempilhar()
    else:
        return "Erro: Expressão RPN inválida - muitos operandos ou operadores"
