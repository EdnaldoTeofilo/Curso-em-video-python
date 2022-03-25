#Melhore o exercício 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
x = int(input('Digite o primeiro termo:'))
y = int(input('Digite a razão da PA:'))
c = 10
z = 1
a = 10
while c > 1:
    if c == 10:
        print('{} '.format(x), end = '')
    x = x + y
    print ('{} '.format(x), end = '')
    c -= 1
z = int(input('\nQuantos termos você quer mostrar a mais? '))
a = a + z
while z > 0:
    x = x + y
    print('{} '.format(x), end = '')
    z -= 1
    if z == 0:
        z = int(input('\nQuantos termos você quer mostrar a mais? '))
        a = a + z

print('\nProgressão finalizada com {} termos mostrados!'.format(a))