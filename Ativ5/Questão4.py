from estruturas_dados import Fila

lista_tarefas = Fila()
print(f"Lista de tarefas inicial: {lista_tarefas}")

lista_tarefas.enfileirar("Comprar pão")
print(f"Após adicionar \'Comprar pão\': {lista_tarefas}")
lista_tarefas.enfileirar("Estudar Estrutura de Dados")
print(f"Após adicionar \'Estudar Estrutura de Dados\': {lista_tarefas}")
lista_tarefas.enfileirar("Fazer exercícios de Python")
print(f"Após adicionar \'Fazer exercícios de Python\': {lista_tarefas}")

print(f"Próxima tarefa a ser concluída: {lista_tarefas.primeiro()}")
print(f"Última tarefa adicionada: {lista_tarefas.ultimo()}")
print(f"Quantidade de tarefas pendentes: {lista_tarefas.tamanho()}")

tarefa_concluida = lista_tarefas.desenfileirar()
print(f"Tarefa concluída: {tarefa_concluida}. Lista atual: {lista_tarefas}")
print(f"Próxima tarefa a ser concluída agora: {lista_tarefas.primeiro()}")
print(f"Quantidade de tarefas pendentes agora: {lista_tarefas.tamanho()}")

tarefa_concluida = lista_tarefas.desenfileirar()
print(f"Tarefa concluída: {tarefa_concluida}. Lista atual: {lista_tarefas}")
print(f"Quantidade de tarefas pendentes agora: {lista_tarefas.tamanho()}")

print(f"A lista de tarefas está vazia? {lista_tarefas.esta_vazia()}")
lista_tarefas.desenfileirar() # Concluindo a última tarefa
print(f"Lista após concluir a última tarefa: {lista_tarefas}")
print(f"A lista de tarefas está vazia? {lista_tarefas.esta_vazia()}")
