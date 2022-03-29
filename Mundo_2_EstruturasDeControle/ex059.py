#Crie um programa que leia dois valores e mostre um menu na tela:
#[1]Somar [2]Multiplicar [3]Maior [4]Novos números [5]sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.
a = 0
x = int(input('Digite o primeiro valor:'))
y = int(input('Digite o segundo valor:'))
c = 0
while c != 5: 
    print('[1]Somar')
    print('[2]Multiplicar')
    print('[3]Maior')
    print('[4]Novos números')
    print('[5]Sair do programa')

    c = int(input('De acordo com o menu escolha:'))
    if c == 1:
        print ('{} + {} = {}'.format(x,y,x+y))
    if c == 2:
        print ('{} x {} = {}'.format(x,y,x*y))
    if c == 3:
        if x > y:
            print('O maior número é:{}'.format(x))
        if y > x:
            print('O maior número é:{}'.format(y))
        else:
            print('Não existe número maior pois os dois números são iguais!')
    if c == 4:
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))
    
print ('FIM!') 
