''' Estudantes.py'''

estudantes = {
    1:{'nome':'joana', 'idade': 45, 'curso': 'Computação'},
    1:{'nome':'Ivan', 'idade': 70, 'curso': 'Matematica'},
    1:{'nome':'Jaqueline', 'idade': 12, 'curso': 'Computação'}
}

cursos = {'Computação', 'Matematica', 'Fisica' }
estudantes_cursos = {
    'Computação':{1,3},
    'Matemática':{2}
}

def adicionarEstudante(matricula,nome,idade,curso):
    pessoa = {'nome': nome, 'idade': idade, 'curso': curso }
    estudantes[matricula] = pessoa
    if curso not in estudantes_cursos:
        estudantes_cursos[curso] = set()
    estudantes_cursos[curso].add(matricula)

# print(estudantes_cursos)
# adicionarEstudante(5, 'Jão', 89, 'Computação')
# print(estudantes_cursos)
# adicionarEstudante(6, 'Maria', 55, 'Fisica')
# print(estudantes_cursos)

print(f'Todas as pessoas matriculadas em algum curso: {estudantes_cursos ['Matemática'] | estudantes_cursos ['Computação']}')
