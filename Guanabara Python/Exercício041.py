#A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos:MIRIM, Até 14 anos:INFANTIL, Até 19 anos:JUNIOR, Até 25 anos:SÊNIOR, Acima Master
from datetime import date

n = int(input('Digite seu ano de nascimento: '))
a = date.today().year
i = a - n
print ('Com a idade de {}'.format(i))
if i <= 9:
    print('Você é da categória MIRIM!')
elif i <= 14:
    print('Você é da categória INFANTIL!')
elif i <= 19:
    print('Você é da categória JUNIOR!')
elif i <= 25:
    print('Você é da categória SÊNIOR!')
else:
    print('Você é da categória MASTER!')