#Crie um programa que faça o computador jogar Jokenpô com você. 
import random 
from time import sleep
print ('Vamos jogar Jokenpô!')
print ('[1] Pedra')
print ('[2] Papel')
print ('[3] Tesoura')
x = int(input('Escolha: '))
print ('JO')
sleep(1)
print ('KEN')
sleep(1)
print ('PÔ!!!')
y = random.choice([1,2,3])
print('A máquina escolheu :{}'.format(y))
if x == 1 and y == 1:
    print('Empate!')
elif x == 1 and y == 2:
    print('Você perdeu!')
elif x == 1 and y == 3:
    print('Você ganhou!')
elif x == 2 and y == 2:
    print('Empate!')
elif x == 2 and y == 1:
    print ('Você ganhou!')
elif x == 2 and y == 3:
    print('Você perdeu!')
elif x == 3 and y == 3:
    print('Empate!')
elif x == 3 and y == 1:
    print('Você perdeu!')
elif x == 3 and y == 2:
    print('Você ganhou!')
else:
    print('Jogada invalida!')