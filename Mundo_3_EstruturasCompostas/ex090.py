#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
x = {}
x ['Nome'] = str(input('Nome: '))
x ['Média'] = float(input(f'Média de {x["Nome"]}: '))
if x["Média"] >= 7:
    x ['Situação'] = 'Aprovado'
else:
    x ['Situação'] = 'Reprovado'
print('*'*30)
for k, v in x.items():
    print(f'{k} é igual a {v}') 