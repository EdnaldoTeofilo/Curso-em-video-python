#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Considere maioridade com 21 anos.
from datetime import date
y = 0
z = 0
a = date.today().year
print (a)
for c in range (0,7):
    x = int(input('Digite a data de nascimento:'))
    if a - x < 21:
        y = y + 1
    else:
        z = z + 1
print ('{} Pessoas atingiram a maioridade!\n{} Pessoas não atigiram sua maioridade!'.format(z,y))