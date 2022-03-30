#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
x = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    y = int(input('Digite um número entre 0 e 20: '))
    if y < 0 or y > 20:
        print('Tente novamente.',end=' ')
    else:
        break
print(f'Você digitou o número {x[y]}.')
 
