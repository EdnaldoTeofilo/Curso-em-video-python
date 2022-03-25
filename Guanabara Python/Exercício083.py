#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
#Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
x = str(input('Digite a expressão: '))
y = []
for a in x:
    if a == '(':
        y.append('(')
    elif a == ')':
        if len(y) > 0:
            y.pop()
        else:
            y.append(')')
            break
if len(y) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
