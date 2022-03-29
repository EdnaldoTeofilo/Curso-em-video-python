#Faça um programa que tenha um função chamada maior(), que receba vários parâmetros com valores inteiros.
#Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep
from winreg import FlushKey


def maior(* núm):
    print ('-='*20)
    print ('Analisando os valores passados...')
    for i in núm:
        print (i, end =' ', flush=True)
        sleep(.2)
    print(f'Foram informados {len(núm)} valores ao todo.')
    x = len(núm)
    if x != 0:
        print(f'O maior valor informado foi {max(núm)}')
    else:
        print('Não existe maior valor!')   

maior (2, 9, 4, 5, 7, 1)
maior (4, 7, 0)
maior (1, -5)
maior (6)
maior ()

