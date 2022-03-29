#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
#No final do programa mostre: A média de idade do grupo. Qual é o nome do homem mais velho. Quantas mulheres tem menos de 20 anos.

a = 0 #idade do homem mais velho 
b = '' #nome do homem mais velho
d = 0 #Soma das idades 
e = 0 #Quantas mulheres tem menos de 20 anos
for c in range (1,5):
    x = str(input('Digite o nome da {}ª pessoa:'.format(c))).strip()
    y = int(input('Digite a idade da {}ª pessoa:'.format(c)))
    print ('[M] para gênero masculino')
    print ('[F] para gênero feminino')
    z = str(input('Digite o sexo da {}ª pessoa:'.format(c))).strip()
    d = d + y
    if z in 'Mm' and c == 1:
        a = y 
        b = x
    if z in 'Mm' and y > a:
        a = y
        b = x
    if z in 'Ff' and y < 20:
        e = e + 1
m = d / 4 # média das idades
print ('A média de idade do grupo é:{}'.format(m))
print ('O nome do homem mais velho tem {} anos e se chama {}'.format(a,b))
print ('Existem {} mulheres que tem menos de 20 anos'.format(e))