#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
from operator import itemgetter
from random import randint
from time import sleep
x = {}
for c in range (1,5):
    x [f'jogador{c}'] = randint(1,6)
print('Valores sorteados:')
for k,v in x.items():
    print(f'O {k} tirou {v}')
    sleep(1)
x = sorted(x.items(), key =itemgetter(1), reverse=True)
print('-=' *20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(x):
    print(f'   {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)
