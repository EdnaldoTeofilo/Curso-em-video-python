#Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#-Equilátero: todos os lados iguais ==== -Isósceles: dois lado iguais ==== -Escaleno: todos os lados diferentes
#Exercício35 = Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

x = int(input('Digite o primeiro segmento: '))
y = int(input('Digite o segundo segmneto: '))
z = int(input('Digite o terceiro segmento: '))
if x < y + z and y < z + x and z < x + y:
    print('Esses segmentos podem formar um triângulo!')
    if x == y == z:
        print('Esse é um triângulo equilátero!')
    elif x == y or y == z or z == x:
        print('Esse é um triângulo isósceles!')
    elif x != y and y != z and z != x:
        print('Esse triângulo é escaleno!')
else:
    print('Esses segmentos não podem formar um triângulo!')