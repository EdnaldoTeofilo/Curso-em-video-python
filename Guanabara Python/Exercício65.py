#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
x = int(input('Digite um número: '))    
a = 'S'
y = 0
z = 0
ma = x
me = x
while a == 'S':
    y += x
    z += 1
    a = str(input('Você deseja inserir outro número [S/N]? ')).upper()
    if a == 'S':
        x = int(input('Digite um número: '))
    if x > ma:
        ma = x
    if x < me:
        me = x

m = y / z
print ('A média entre todos os valores foi: {:.2f}'.format(m))
print ('O maior número foi: {}'.format(ma))
print ('O menor número foi: {}'.format(me))

