#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#Ex: Digite um número: 1834 //// unidade:4 dezena:3 centena:8 milhar:1
x = int(input('Digite um número: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print ('Unidade: {}'.format(u))
print ('Dezena: {}'.format(d))
print ('Centena: {}'.format(c))
print ('Milhar: {}'.format(m))
#Daria para fazer em string e pegar a posição tbm mas teria alguns problemas se a resposta não fosse com 4 dígitos