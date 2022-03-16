#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))
if x > y and x > z:
    maior = x
if y > x and y > z:
    maior = y
if z > x and z > y:
    maior = z
if x < y and x < z:
    menor = x
if y < x and y < z:
    menor = y
if z < x and z < y:
    menor = z
print ('O maior número é: {}'.format(maior))
print ('O menor número é: {}'.format(menor))