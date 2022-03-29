#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.
x = '' 
while x != 'M' and x != 'F':
    x = str(input('Qual seu sexo [M/F]:')).strip().upper()