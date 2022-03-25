#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

c = float(input('Valor da casa: '))
s = float(input('Salário do comprador: '))
a = int(input('Quantos anos de financiamento: '))
m = a*12 #Ano convertido em meses
p = c/m  #Valor da parcela
print ('Para pagar um casa de R${} em {} anos a prestação será de:R${:.2f}'.format(c,a,p))
if p <= s*0.3: 
    print ('Empréstimo pode ser CONCEDIDO!')

else:
    print ('Empréstimo NEGADO.')
