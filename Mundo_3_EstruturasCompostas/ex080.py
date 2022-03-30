#Crie um programa onde o usuário possa digitar cinco valores númericos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
#No final, mostre a lista ordenada na tela.
x = []
for c in range (0, 5):
    y = int(input('Digite um número: '))
    if c == 0 or y > x[-1]:
        x.append(y)
    else:
        pos = 0
        while pos < len(x):
            if y <= x[pos]:
                x.insert(pos, y)
                break
            pos += 1
print('=-'*30)
print(f'Os números digitados em ordem foi: {x}')

     