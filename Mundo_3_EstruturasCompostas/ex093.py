'''Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos em cada partida'''
x = {}
y = []
z = 0
x ['nome'] = str(input('Nome do Jogador: '))
a = int(input(f'Quantas partidas {x ["nome"]} jogou? '))
for i in range (1,a + 1):
    y.append(int(input(f'Quantos gols na partida {i}? ')))
    z += y[i-1]
x ['gols'] = y.copy()
x ['total'] = z
print ('-='*30)
print (x)
print ('-='*30)
for k,v in x.items():
    print(f'O campo {k} tem valor {v}.')
print('-='*30)
print(f'O jogador {x ["nome"]} jogou {x ["total"]} partidas.')
for i in range (1,a + 1):
    print(f'  => Na partida {i}, fez {y[i-1]} gols.')
print (f'Foi um total de {x ["total"]} gols.')
 