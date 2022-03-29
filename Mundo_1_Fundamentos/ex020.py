#O mesmo professor do desario anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia dos quatro alunos e mostre a ordem sorteada
import random 
a = input('Digite o nome do primeiro aluno:')
b = input('Digite o nome do segundo aluno:')
c = input('Digite o nome do terceiro aluno:')
d = input('Digite o nome do quarto aluno:')
x = [a,b,c,d]
random.shuffle(x)
print('A ordem sorteada foi: {}'.format(x))