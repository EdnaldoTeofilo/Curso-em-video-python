#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto    -À vista no cartão:5% de desconto     -Em até 2x no cartão:Preço normal     -3x ou mais no cartão:20% de juros

x = float(input('Digite o valor do produto: R$'))
print('1)à vista dinheiro/cheque: 10% de desconto')
print('2)À vista no cartão:5% de desconto')
print('3)Em até 2x no cartão:Preço normal')
print('4)3x ou mais no cartão:20% de juros')
y = int(input('Escolha sua forma de pagamento 1/2/3/4: '))
if y == 1:
    print('O valor a ser pago será de: R${:.2f}'.format(x*0.9))
elif y == 2:
    print('O valor a ser pago será de: R${:.2f}'.format(x*0.95))
elif y == 3:
    print('O valor a ser pago será de: R${:.2f}'.format(x))
elif y == 4:
    z = int(input('Quantas parcelas?'))
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(z,((x*1.2)/z)))
    print('O valor a ser pago será de: R${:.2f}'.format(x*1.2))