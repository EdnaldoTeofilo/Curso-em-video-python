#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
#No final, mostre os valores pares e ímpares em ordem crescente.
y = [[], []]
for c in range (1,8):
    x = int(input(f'Digite o {c}º número: '))
    if x % 2 == 0:
        y[0].append(x)
    else:
        y[1].append(x)
print ('-='*30)
y[0].sort()
y[1].sort()
print(f'Os valores pares digitados foram: {y[0]}')
print(f'Os valores ímpares digitados foram: {y[1]}')
