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

adicionaTarefa('Arrumar a cama')
adicionaTarefa('Lavar a louça')
exibeTarefas()
print('Agora vou concluir...')
concluirTarefa('Arrumar a cama')
exibeTarefas()

#=============================================================#

lista1 = [1,5,9]
novaLista1 = [n * 2 for n in lista1]
novaLista1 = [n * 2 for n in lista1 if n > 4] 
novaLista1 = [n * 2 for n in lista1 if n > 7] #for dentro da lista

print(novaLista1)

#=============================================================#

[n for n in range(11)]
[n for n in range(11) if n % 2 == 0]

#=============================================================#

frutas = ['pera','uva','maçã']
[f for f in frutas]
[ f.upper() for f in frutas ]
print(frutas)

#=============================================================#

[(n,n * 3) for n in range(1,11)]

#=============================================================#

