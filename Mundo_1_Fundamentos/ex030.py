# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

x = int(input('Digite um número: ')) 
y = x % 2
if y == 0:
    print('O número {} é par'.format(x))
else:
    print('O número {} é ímpar'.format(x))
