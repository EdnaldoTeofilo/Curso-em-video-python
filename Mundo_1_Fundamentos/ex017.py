#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.
from math import hypot
x = int(input('Digite o comprimento do cateto oposto: '))
y = int(input('Digite o comprimento do cateto adjacente: '))
print ('A hipotenusa dos catetos {} e {} é igual a {:.2f}'.format(x,y,hypot(x,y)) )