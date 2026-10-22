print('Bem-vindo ao Detran')
print('Este é o novo teste para liberar ou não a CNH')
print()
idade = int(input('Digite a sua idade: '))

# se a idade for maior do que 18, então
#     deixa dirigir
# senao
#     não deixa

if idade >= 18:
    print('estar aprovado para a cnh')
else:
    print('não estar aprovado para a cnh')