#Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
import random
a = random.randint(1,10)
b = random.randint(1,10)
c = random.randint(1,10)
d = random.randint(1,10)
e = random.randint(1,10)
x = (a, b, c, d, e)
z = (int)
print (f'Os números sorteados foram: {x}')
'''ma = 0
me = 11
for cont in range(0, len(x)):
    if x[cont] > ma:
        ma = x[cont]
    if x[cont] < me:
        me = x[cont]
print(f'O maior número gerado foi: {ma}')
print(f'O menor número gerado foi: {me}')'''
print(f'O maior número gerado foi: {max(x)}')
print(f'O menor número gerado foi: {min(x)}') 