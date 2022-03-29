#Crie um programa que leia de idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
#No final, mostre: Quantas pessoas tem mais de 18 anos. Quantos homens foram cadastrados. Quantas mulhers tem menos de 20 anos.
M = h = m = 0
while True:
    print ('='*30) 
    print ('Cadastre uma pessoa')
    print ('='*30)
    while True:
        i = input('Idade: ').strip()
        if i.isnumeric() == True:
            break
        if i.isnumeric() == False:
            print('Utilize número.Exemplo: 18')
    i = int(i)    
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]:')).upper().strip()[0]
    print ('='*30)
    if i >= 18:
        M += 1
    if s == 'M':
        h += 1
    if s == 'F' and i < 20:
        m += 1
    x = ' '
    while x not in 'SN':
        x = str(input('Você quer continuar [S/N]? ')).upper().strip()[0]
    if x == 'N':
        break
print (f'{M} pessoas tem 18 anos ou mais.')
print (f'{h} homens foram cadastrados.')
print (f'{m} mulheres tem menos de 20 anos.') 
