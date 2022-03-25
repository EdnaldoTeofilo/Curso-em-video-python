#Faça um programa que leia um número qualquer e mostre o seu fatorial.
'''from math import factorial'''
x = int(input('Digite um número para calcular seu fatorial:'))
'''c = factorial(x)
print('{}'.format(c))'''
c = x
z = 1
print('Calculado {}! = '.format(x), end = '')
while c > 0:
    print('{}'.format(c), end = '')
    if c > 1:
       print(' x ', end = '')
    else:
        print(' = ', end = '')
    z = z * c
    c -= 1
print ('{}'.format(z))