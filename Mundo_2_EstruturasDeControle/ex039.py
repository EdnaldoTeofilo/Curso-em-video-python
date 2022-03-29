#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar ao serviço militar. Se é a hora de se alistar. Se já passou o tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo. 
from datetime import date
x = int(input('Digite seu ano de nascimento: '))
z = date.today().year
i = z-x

print('Quem nasceu em {} tem {} anos em 2022.'.format(x,i))

if i < 18:
    print('Ainda faltam {} anos para o alistamento'.format(18-i))
elif i == 18:
    print('Você tem que se alistar esse ano.')
else:
    print('Você já {} anos do seu prazo de alistamento.'.format(i-18))