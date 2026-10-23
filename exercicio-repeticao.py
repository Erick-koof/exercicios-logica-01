soma = 0
n = 1

# while n <= 10:
#     soma = soma + n   ---> 1° metodo
#     n = n + 1
# print(f'soma: {soma}')
# print(f'n: {n}')

# for index in range(1,11):
#     print('index')        ---> 2° metodo
#     soma = soma + n
#     n = n + 1

# versão mais simplificada:
# for index in range(1,11):
#     soma = soma + index


# versão mais simplificada , mais simples:
for index in range(1,11):
    soma += index

# ultimate simplificado: menor que isso eu não sei se existe!!?
# soma = sum([i for i in range(1,11)])

print(f'a soma dos numeros de 1 a 10 é: {soma}')


