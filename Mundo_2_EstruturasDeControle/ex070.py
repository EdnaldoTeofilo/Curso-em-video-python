#Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
#No final, mostre: A)Qual é o total gasto na compra. B)Quantos produtos custam mais de R$1000. C)Qual é o nome do produto mais barato.
total = acima = a = 0
barato = ''
while True:
    x = str(input('Nome do produto: '))
    y = int(input('Digite o preço: '))
    if a == 0:
        a = y
        barato = x
    if a > y:
        a = y
        barato = x
    total += y
    if y > 1000:
        acima += 1
    z = ' '
    while z not in 'SN':
        z = str(input('Deseja continuar [S/N]? ')).upper().strip()
    if z == 'N':
        break
print (f'Total da compra: R${total:.2f}')
print (f'Total de produtos acima de R$1000: {acima}')
print (f'O produto mais barato: {barato}')