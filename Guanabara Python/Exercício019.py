#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
from random import choice
a = input('Digite o nome do primeiro aluno:')
b = input('Digite o nome do segundo aluno:')
c = input('Digite o nome do terceiro aluno:')
d = input('Digite o nome do quarto aluno:')
print('O aluno escolhido para apagar o quadro foi: {}'.format(choice([a,b,c,d])))