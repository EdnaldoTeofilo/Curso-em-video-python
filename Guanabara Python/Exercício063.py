#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci
print ('#'*30)
print ('Sequência de Fibonacci')
print ('#'*30)
x = int(input('Quantos termos você deseja ver:'))
t1 = 0
t2 = 1
y = 1
while y <= x:
    if y == 1:
        print(' {},'.format(t1), end = '')
        y += 1
    if y == 2:
        print(' {},'.format(t2), end = '')
        y += 1
    t3 = t1 + t2
    print (' {},'.format(t3), end = '')
    t1 = t2
    t2 = t3
    y += 1
print (' FIM!')