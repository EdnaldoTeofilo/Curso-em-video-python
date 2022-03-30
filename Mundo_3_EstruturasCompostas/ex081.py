#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre: A)Quantos números foram digitados. B)A lista de valores, ordenada de forma decrescente. C)Se o valor 5 foi digitado e está ou não na lista.
x = []
while True:
    x.append(int(input('Digite um número: ')))

    y = ' '
    while y not in 'N' and y not in 'S':
        y = str(input('Você deseja continuar? [S/N]')).upper().strip()
    if y == 'N':
        break

x.sort(reverse=True)

print(f'Você digitou {len(x)} elementos.')
print(f'Os valores em ordem decrescente são {x}')

if 5 in x:
   print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')
 