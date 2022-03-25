#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas gerados.
x = []

while True:
    x.append(int(input('Digite um número: ')))
    y = ' '
    while y not in 'S' and y not in 'N':
        y = str(input('Você deseja continuar? [S/N] ')).upper().strip()
    if y == 'N':
        break

a = 0
par = []
i = []

while a < len(x):
    if x[a] % 2 == 0:
        par.append(x[a])
    else:
        i.append(x[a])
    
    a += 1
print ('=-'*30)
print(f'Os valores digitados foram {x}')
print(f'Os valores digitados pares {par}')
print(f'Os valores digitados ímpares {i}')
