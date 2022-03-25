#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
x = float(input('Digite o primeiro segmento: '))
y = float(input('Digite o segundo segmento: '))
z = float(input('Digite o terceiro segmento: '))
if x < y + z and y < x + z and z < x + y:
    print('Esses segmentos podem formar um triângulo!!!')
else:
    print('Esses segmentos não podem formar um triângulo!!!')
                                                         
