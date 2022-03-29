#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e somaPar().
#A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep

def sorteia():
    for i in range (0,5):
        números.append(randint(1,100))
    print('Sorteando 5 valores da lista: ', end='')
    for i in números:
        print(i, end=' ',flush=True)
        sleep(.3)
    print('PRONTO!')

def somaPar():
    s = 0
    for p in números:
        if p % 2 == 0:
            s += p
    print(f'Somando os valores pares de {números}, temos {s}.')

números = []       
sorteia()
somaPar()
