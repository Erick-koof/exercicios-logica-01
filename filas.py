from collections import deque

def criaFila():
    return deque()

def insereNaFila(fila, elemento):
    fila.append(elemento)

def removeDaFila(fila):
    return fila.popleft()



fila = criaFila()

print(fila)
insereNaFila(fila, 1)
insereNaFila(fila, 2)
insereNaFila(fila, 3)
insereNaFila(fila, 4)
insereNaFila(fila, 5)
print(f'Removendo: {removeDaFila(fila)}')
print(f'Removendo: {removeDaFila(fila)}')
print(fila)

#deck double end kill ---> fila com duas entradas