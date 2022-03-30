#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
#No final, mostre: A) Quantas pessoas foram cadastradas. B) A média de idade do grupo.
#C) Uma lista com todas as mulhers. D) Uma lista com todas as pessoas com idade acima da média.'''
x = {}
y = []
m = float()
while True:
    x ['nome'] = str(input('Nome: '))
    x ['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    while x ['sexo'] not in 'MF':
        x ['sexo'] = str(input('Sexo: [M/F] ')).upper()
    x ['idade'] = int(input('Idade: '))
    z = ' '
    while z not in 'S' and z not in 'N':
        z = str(input('Quer continuar? [S/N] ')).upper().strip()
    y.append(x.copy())
    m += x ['idade']
    if z == 'N':
        break
m = m / len(y)
print ('-='*30)
print(y)
print ('-='*30)
print (f'A) O grupo tem {len(y)} pessoas.')
print (f'B) A média de idade é de {m:.2f} anos.')
print ('C) As mulheres cadastradas foram: ', end='')
for i in y:
    if i ['sexo'] == 'F':
        print (f'{i ["nome"]}, ', end='')
print ('\nD) Lista das pessoas que estão acima da média:')
for i in y:
    if i ['idade'] >= m:
        print()
        for k,v in i.items():
            print (f'{k} = {v}; ', end='')
        print()
print ('FIM!!!')

 