# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.
x = int(input('Qual a distância da viagem em Km: '))
if x<= 200:
    print('O preço da passagem será: R${:.2f}'.format(x*0.5))
else:
    print('O preço da passagem será: R${:.2f}'.format(x*0.4))