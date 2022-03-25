#Refaça o Exercício 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while. 
x = int(input('Digite o primeiro termo:'))
y = int(input('Digite a razão da PA:'))
c = 10

while c > 1:
    if c == 10:
        print('{} '.format(x), end = '')
    x = x + y
    print ('{} '.format(x), end = '')
    
    c -= 1
