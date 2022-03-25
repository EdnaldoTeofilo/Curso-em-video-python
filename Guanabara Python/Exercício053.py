#Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços.
x = (input('Digite uma frase: ')).lower().strip()
y = x.split()
z = ''.join(y)
if z == z[::-1]:
    print('É um políndromo!')
else:
   print('Não é um políndromo!')
