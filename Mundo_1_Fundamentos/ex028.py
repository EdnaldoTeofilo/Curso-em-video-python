#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escollhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
import random
x = random.randint(0,5)
y = int(input('Digite um número entre 0 e 5 e descubra se foi o mesmo escolhido pelo computador:'))
if x == y:
    print('Parabéns você acertou!!!')
else:
    print('Você errou!!!')