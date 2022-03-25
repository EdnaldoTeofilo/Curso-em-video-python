#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal, 3 para hexadecimal

x = int(input('Digite um número: '))
y = int(input('Digite 1 para binário, 2 para octal, 3 para hexadecimal:'))

if y==1:
    print('O número {} em binário é: {}'.format(x,bin(x)))
elif y==2:
    print('O número {} em octal é: {}'.format(x,oct(x)))
else:
    print('O número {} em hexadecimal é: {}'.format(x,hex(x)))
