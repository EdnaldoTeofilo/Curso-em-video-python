#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
#No final, mostre: A)Quantas pessoas foram cadastradas. B)Uma listagem com as pessoas mais pesadas. C)Uma listagem com as pessoas mais leves.
x = []
pc = []
ma = me = 0
pesoma = []
pesome = []
while True:
    x.append(str(input('Nome: ')))
    x.append(float(input('Peso: ')))
    pc.append(x[:])
    x.clear()
    y = ' '
    while y not in 'S' and y not in 'N':
        y = (str(input('Quer continuar? [S/N] '))).upper().strip()
    if y == 'N':
        break
for c in pc:
    
    if c == pc[0]:
        ma += c[1]
        me += c[1]
    else:
        if c[1] > ma:
            ma = c[1]
        if c[1] < me:
            me = c[1]
for c in pc:

    if c[1] == ma:
        pesoma.append(c[0])
    if c[1] == me:
        pesome.append(c[0])
    
print (f'Foram cadastradas {len(pc)} pessoas.')
 
print (f'O maior peso foi de {ma}Kg.', end='')
print (f'Peso de {pesoma}', end=' ')

print (f'\nO menor peso foi de {me}Kg.', end='')
print (f'Peso de {pesome}', end=' ')
