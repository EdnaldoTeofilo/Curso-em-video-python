#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.EX: Digite um número:6.127 ----- O número 6.127 tem a parte Inteira 6.
from math import floor # Da para importa apenas uma parte ou partes do módulo, assim não precisando usar mais math.floor e usando apenas floor
x = float(input('Digite um número:'))
print ('O número {} tem a parte Inteira {}'.format(x,floor(x)))
 