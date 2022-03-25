#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
x = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
print('-'*30)
for c in x:
    print(f'\nNa palavra {c} temos', end=' ')
    for l in c:
        if l in 'AaEeIiOoUu':
            print(l,end =' ')
