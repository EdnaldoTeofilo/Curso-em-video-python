#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o. 
x = 0
for c in range (0,6):
    y = int(input('Digite um número:'))
    if y % 2 == 0:
        x = x + y
print('A soma de todos os números pares é: {}'.format(x))

