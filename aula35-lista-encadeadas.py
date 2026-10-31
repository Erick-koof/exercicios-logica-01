lista = None

def exibeLista():
    if not lista:
        print('Lista vazia.')
        return
    elemento = lista

    while elemento != None:
        print(elemento['valor'], end=' ')
        elemento = elemento['proximo']

    print('.')

def adicionaNoFim( elemento):
    global lista
    if not lista:
        lista = {'valor':elemento, 'proximo': None}
        return
    atual = lista
    while atual['proximo']:
        atual = atual['proximo']
    atual['proximo'] = {'valor': elemento, 'proximo': None}

exibeLista()
print('Adicionando o 1...')
adicionaNoFim(1)
exibeLista()
print('Adicionando o 2...')
adicionaNoFim(2)
exibeLista()
print('Adicionando o 3...')
adicionaNoFim(3)
exibeLista()
print('Adicionando o 4...')
adicionaNoFim(4)
exibeLista()
print('Adicionando o 5...')
adicionaNoFim(5)
exibeLista()

print(lista)