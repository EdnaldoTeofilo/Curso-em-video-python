#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250.00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15%.
x = float(input('Digite o seu salário: '))
if x > 1250:
    print('Seu salário de R${} com aumento de 10% é: R${:.2f}'.format(x,x*1.1))
else:
    print('Seu salário de R${} com aumento de 15% é: R${:.2f}'.format(x,x*1.15))