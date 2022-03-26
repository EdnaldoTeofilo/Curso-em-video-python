#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Coloque o valor do produto: '))
novo = preço * 0.95
print(f'O produto que custava R${preço}, na promoção com descontro de 5% vai custar R${novo:.2f}.')