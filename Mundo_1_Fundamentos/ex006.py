#Crie um algoritmo que leia um número e mostre o seu dobro,  triplo e raiz quadrada.
x = int(input('Digite um número: '))
d = x * 2
t = x * 3
r = x ** (1/2)
print(f'O dobro de {x} vale {d}.')
print(f'O triplo de {x} vale {t}')
print(f'A raiz quadrada de {x} é igual a {r:.2f}')