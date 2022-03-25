#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint
from time import sleep
x = []
print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)
y = int(input('Quantos jogos você quer que eu sorteie? '))
str= (f"SORTEANDO {y} JOGOS")
print (f'{str:^30}')
for j in range (1,y+1):
    for ms in range (0,7):
        x.append(randint(1,60))
    print(f'Jogo {j}: {x}')
    sleep(.5)
    x.clear()
print (f"{'BOA SORTE!':^30}")

