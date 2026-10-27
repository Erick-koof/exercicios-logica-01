# Estruturas de dados pre-definidas

# - Listas: conjunto de dados ordenados - mutável
lista = [1,2,3,4]
frutas = ['banana', 'maça']
mista = [1, 'texto', 5, True]

# - Tuplas: conjunto de dados ordenados - imultável
coordenada = (5,6)
tupla = (5,4,3,2,1)

# - Dicionários (dict): conjunto de pares na forma chave e valor
pessoa = {'nome: ': 'joão', 'idade':18}
carro = {
    'marca': 'volks',
    'modelo': 'fusca',
    'cor': 'azul',
    'ano': 1970
}


# - Conjuntos (sets): Conjunto de dados não ordenados e sen repetição
c1 = {1,2,3}
c2 = {3,2,1}
c3 = {1,1,1,2,2,2,3,3,3}


# tira a medias das notas:
notas = [3,7,8,10]
sum(notas)
len(notas)
media = sum(notas) / len(notas)
print(media)