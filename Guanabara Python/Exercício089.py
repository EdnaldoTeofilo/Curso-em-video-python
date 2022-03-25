#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
x = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    x.append([nome, [nota1, nota2], media])
    y = ' '
    while y not in 'S' and y not in 'N':
        y = str(input('Quer continuar? [S/N] ')).upper().strip()
    if y == 'N':
        break
print('-='*20)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('='*26)
for i, a in enumerate(x):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    z = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if z == 999:
        break
    elif z <= len(x) - 1:
        print(f'Notas de {x[z][0]} são {x[z][1]}')

print('FIM!')
