#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
x = []
while True:
    
    y = int(input('Digite um valor: '))
    
    if y not in x:
        x.append(y)
    else:
        print('Valor duplicado! Não vou adicionar...')
    
    z = ' '
    while z not in "S" and z not in "N":
        z = str(input('Quer continuar? [S/N]')).upper().strip()
    if z == 'N':
        break
print (" :) "*10)    
x.sort()
print(f'Os valores digitados em ordem crescente foram: {x}')