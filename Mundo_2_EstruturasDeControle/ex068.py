#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
import random
print ('='*30) 
print ('Jogar ìmpar ou par :)')
print ('='*30)
a = c = 0
b = ' '

while True:
    while True:
        y = input('Digite um número: ')
        if y.isnumeric() == True:
            break
    y = int(y)
    z = ' '
    while z not in 'I' and z not in 'P':
        z = str(input('Ímpar ou Par? [I/P]')).upper().strip()
    print ('-'*30)
    x = random.randint(0,10)
    a = x + y
    if a % 2 == 0:
        b = 'PAR'
    else:
        b = 'IMPAR'
    print (f'Você jogou {y} e o computador {x}. Total de {a} deu {b} ')
    print ('-'*30)
    if z == 'I' and b == 'IMPAR' or z == 'P' and b == 'PAR':
        print ('Você VENCEU!')
        c += 1
    else:
        print ('Você PERDEU!')
        break
print(f'GAME OVER! Você venceu {c} vezes.') 

