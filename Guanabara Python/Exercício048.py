#Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.
x = 0
for c in range (1,501,2):
    
    if c%3 == 0:
        x = x + c
print('A soma de todos os números ímpares que são múltiplos de três é:{}'.format(x))
