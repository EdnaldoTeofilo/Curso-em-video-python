#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
#No final, mostre quantos números foram digitados e qual foi a soma entre eles(desconsiderando o flag.)
y = z = 0
while True:
    x = int(input('Digite um número: '))
    if x == 999: 
        break
    y += x
    z += 1
print(f'Foram digitados {z} números e a soma deles é de {y}')