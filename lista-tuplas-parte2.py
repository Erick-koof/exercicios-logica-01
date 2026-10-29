""" Gerenciador de Tarefas"""

tarefas = []

def adicionaTarefa(tarefa):
    novaTarefa = (tarefa, 'pendente')
    tarefas.append(novaTarefa)

def exibeTarefas():
    for tarefa in tarefas:
        print(f'{tarefa[0]} - Status: {tarefa[1]}')

def concluirTarefa(tarefa):
    global tarefas
    tarefa = [(t[0], 'concluida') if t[0] == tarefa else t for t in tarefas]

def removerTarefa(tarefa):
    global tarefas
    tarefas = [ t for t in tarefas if t[0] != tarefa] 

def buscarTarefa(tarefa):
    resultado = [t for t in tarefas if t[0].lower() == tarefa.lower()]
    if resultado:
        for titulo,status in resultado:
            print(f'Encontrada: {titulo} - Status: {status}')
    else:
        print(f'Tarefa não encontrada: {tarefa}')


adicionaTarefa('Arrumar a cama')
adicionaTarefa('Lavar a louça')
exibeTarefas()

buscarTarefa('Arruma a cama')
buscarTarefa('Ir ao mercado')