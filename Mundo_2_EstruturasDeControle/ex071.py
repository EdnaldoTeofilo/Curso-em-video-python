#Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#OBS:Considere que o caixa possui cédulas de R$50,R$20,R$10 e R$1.
from time import sleep
while True:
    print ('='*16)
    print ('CAIXA ELETRÔNICO')
    print ('='*16)
    while True:
        x = input('Digite o valor a ser sacado? R$')
        if x.isdigit() == True:
            x = int(x)
            break
    c = v = d = u = 0
    if x // 50 > 0:
        c = x // 50
        x = x % 50
    if x // 20 > 0:
        v = x // 20
        x = x % 20
    if x // 10 > 0:
        d = x // 10
        x = x % 10
    if x // 1 > 0:
        u = x // 1
    print('Calculando notas...')
    sleep(1)
    if c > 0:
        print (f'Total de {c} cédulas de R$50')
    if v > 0:
        print (f'Total de {v} cédulas de R$20')
    if d > 0:
        print (f'Total de {d} cédulas de R$10')
    if u > 0:
        print (f'Total de {u} cédulas de R$1')   
    a = ' '
    while a not in 'SN':
        a = str(input('Você deseja continuar [S/N]? ')).upper().strip()
    if a == 'N':
        break
print('Obrigado e volte sempre!')