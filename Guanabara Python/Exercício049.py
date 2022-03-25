#Refaça o exercício9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
x = int(input('Digite um número para saber sua tabuada:'))
for c in range (1,10):
    print('{} x {} = {}'.format(x,c,x*c))