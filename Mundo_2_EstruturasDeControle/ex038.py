#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
#O primeiro valor é maior, o segundo valor é maior, não existe valor maior, os dois são iguais 
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

if x > y:
    print('O primeiro valor é maior')
elif x < y:
    print('O segundo número é maior')
else:
    print('Não existe valor maior, os dois são iguais') 