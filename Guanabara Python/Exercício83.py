#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''Jeito errado na tentativa de ex: )a+b('''
x = input('Digite a expressão: ')
y = x.count("(")                            
z = x.count(")")                            
if y != z:
    print('A expressão está errada!')
else:
    print('A expressão está válida!')