#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
import math 
a = float(input('Digite o ângulo: '))
x = math.radians(a)
print('O valor de seno: {:.2f}\nO valor do cosseno: {:.2f}\nO valor da tangente: {:.2f}'.format(math.sin(x),math.cos(x),math.tan(x)))
