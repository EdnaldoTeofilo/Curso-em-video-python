'''Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobrar() e metade().
Faça também um programa que importe esse módulo e use algumas dessas funções.'''

from ex107_modulo import moeda

valor = float(input('Digite o preço: R$ '))

print(f'A metade de R${valor} é R${moeda.metade(valor):.2f}')
print(f'O dobro de R${valor} é R${moeda.dobro(valor):.2f}')
print(f'Aumentando 10%, temos R${moeda.aumentar(valor,10):.2f}')
print(f'Diminuindo 13%, temos R${moeda.diminuir(valor,13):.2f}')