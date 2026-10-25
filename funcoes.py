# def olamundo():
#     print('Olá, mundo!')

# olamundo()



# def olaPessoa(nome): # variavel de entrada (nome)
#     print(f'Olá, {nome}')

# olaPessoa('Erick')


# def dobro(numero):
#     return numero * 2
# print(dobro(5) + 2)



# def multiplicadoisnumeros(a,b):
#     return a * b
# print(multiplicadoisnumeros(3,6))
# print(multiplicadoisnumeros(3))



# def multiplicadoisnumeros(a,b = 2): #valor padrão (b = 2) / não pode fazer ao contrario (a = 2)
#     ''' Multiplica dois numeros'''
#     return a * b
# print(multiplicadoisnumeros(3,6))
# print(multiplicadoisnumeros(3))


x = 5  #variável global
def soma():
    x = 10  #variável local
    print(x)
    return x + 1
soma()
print(x)