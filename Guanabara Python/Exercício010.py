#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
x = float(input('Digite o valor do seu saldo em reais? R$'))
d = x / 5.27
print (f'Com o dolar valendo 5.27 seu saldo de R${x:.2f} seria de USD${d:.2f} dolares')