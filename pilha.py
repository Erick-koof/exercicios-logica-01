from collections import deque

def criaPilha():
    return deque()

def insereNaPilha(pilha, elemento):
    pilha.append(elemento)

def removeDaPilha(pilha):
    return pilha.pop()

pilha = criaPilha()

print(pilha)
insereNaPilha(pilha, 1)
insereNaPilha(pilha, 2)
insereNaPilha(pilha, 3)
insereNaPilha(pilha, 4)
insereNaPilha(pilha, 5)
print(f'Removendo: {removeDaPilha(pilha)}')
print(f'Removendo: {removeDaPilha(pilha)}')
print(pilha)

#deck double end kill ---> fila com duas entradas