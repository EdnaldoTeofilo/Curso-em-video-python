# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
x = str(input('Digite seu nome completo: ')).strip()
y = (x.split()) 
print('Seu primeiro nome é: {}'.format(y[0]))
print('Seu último nome é: {}'.format(y[len(y)-1]))