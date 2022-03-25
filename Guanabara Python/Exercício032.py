# Faça um programa que leia um ano qualquer e mostre se ele é bissexto. Ocorrendo a cada quatro anos (exceto anos múltiplos de 100 que não são múltiplos de 400).
x= int(input('Digite um ano: '))
if x % 4 == 0 and x % 100 !=0 or x % 400 ==0:
    print ('O ano {} é um ano bissexto'.format(x))
else:
    print ('O ano {} não é bissexto'.format(x))