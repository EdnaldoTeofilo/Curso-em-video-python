#Melhore o jogo do exercício 28 onde o computador vai "pensar" em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
z = 1 #Quantos palpites foram necessários
x = random.randint(0,10)
y = 11
while not y == x:
    y = int(input('Tente adivinhar o número que a máquina pensou entre 1 e 10:'))
    if y != x:
        z = z + 1
if z > 1:
    a = 'tentativas'
else:
    a = 'tentativa'

print('Parabéns você venceu com um total de {} {} para vencer!'.format(z,a))