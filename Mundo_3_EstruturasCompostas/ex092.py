#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. 
#Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
#Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
from datetime import datetime
x = {}
x ['nome'] = str(input('Nome: '))
y = int(input('Ano de nascismento: '))
x ['idade'] = datetime.now().year - y
x ['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if x ['ctps'] != 0:
    x ['contratação'] = int(input('Ano de contratação: '))
    x ['salário'] = float(input('Salário: R$'))
    x ['aposentadoria'] = x ['idade'] + ((x ['contratação'] + 35) - datetime.now().year)
for k,v in x.items():
    print (f' {k} tem valor {v}')