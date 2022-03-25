#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
#No final, mostre uma listagem de preços, organizando os dados em forma tabular.
x = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print ('-'*40)
print (f'{"LISTAGEM DE PREÇOS":^40}')
print ('-'*40)
for c in range (0,len(x)):
    if c % 2 == 0:
        print(f'{x[c]:.<30}', end='')
    else:
        print(f'R${x[c]:7.2f}')
print ('-'*40)