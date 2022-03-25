#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salário = float(input('Digite o valor do seu salário: '))
novo = salário * 1.15
print (f'Um funcionário que ganhava R${salário}, com 15% de aumento, passa a receber R${novo:.2f}.')