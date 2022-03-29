#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
x = int(input('Digite um número [999 para parar]: '))
y = 0
z = 0
while x != 999: 
    y += x
    z += 1
    x = int(input('Digite um número: '))
print('Foram digitados {} números e a soma deles foi de {}'.format(z,y))