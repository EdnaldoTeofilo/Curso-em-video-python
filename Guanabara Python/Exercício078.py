#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
x =[]
for c in range(1,6):
    x.append(int(input(f'Digite um número para a posição {c}: ')))
print('=-'*20)
print(f'Você digitou os valores {x}')
print(f'O maior número digitado foi {max(x)} nas posições ', end ='')
for i,v in enumerate(x):
    if v == max(x):
        print(f'{i}...', end= '')

print(f'\nO menor número digitado foi {min(x)} nas posições ', end ='')
for i,v in enumerate(x):
    if v == min(x):
        print(f'{i}...', end ='')
