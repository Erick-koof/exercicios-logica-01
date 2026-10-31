frase = 'O curso de lógica de Programação é fácil!'
# print(f'Primeira letra: {frase[0]}')
# print(f'Ultima letra: {frase[-1]}')
# print(f'Tamanho da frase: {len(frase)} caracteris')
# print()
# print(f'Maiúsculas: {frase.upper()}')
# print(f'Minúsculas: {frase.lower()}')
# print()
# print(f'Fatiando: {frase.split()}')
# print(f'Fatiando: {frase.split('a')}')
# print()
# print(f'Frase original: {frase}')
# print(f'Limpando: {frase.strip()}')
# print(f'Tamanho da string limpa: {len(frase.strip())}')


def analisadorDeTexto(texto):
    palavras = texto.split()
    num_palavras = len(palavras)
    num_caractes = len(texto)
    num_caracteres_sem_espacos = num_caractes - texto.count(' ')
    return num_palavras, num_caractes, num_caracteres_sem_espacos

num_p, num_c, num_cse = analisadorDeTexto(frase)
print(f'Num palavras: {num_p}')
print(f'Num caracteres: {num_c}')
print(f'Num caracteres sem espaço: {num_cse}')