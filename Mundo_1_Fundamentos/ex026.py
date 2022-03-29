# Faça um programa que leia uma frase pelo teclado e mostre: Quantas vezes aparece a letra "A". Em que posição ela aparece a primeira vez. Em que posição ela aparece a última vez.
x = str(input('Digite uma frase: ')).upper().strip()
 
print ('A letra A aparece {} vezes na frase'.format(x.count('A')))
print ('A primeira letra A apareceu na posição {}'.format(x.find('A')+1))
print ('A última letra A apareceu na posição {}'.format(x.rfind('A')+1))
