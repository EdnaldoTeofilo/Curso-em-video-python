#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

x = int(input('Quantos dias alugados?')) 
y = float(input('Quantos Km rodados?'))
z = (60*x)+(0.15*y)
print('O total a pagar é de R${:.2f}'.format(z))