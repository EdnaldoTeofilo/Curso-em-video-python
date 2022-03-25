#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
y = 0
z = 0

for c in range (1,6):
    x = float(input('Digite o peso da {}º pessoa:'.format(c)))
    if c == 1:
        y = x
        z = x
    else:
        if x > y:
            y = x
        elif x < z:
            z = x
print('O maior peso lido foi:{:.2f}Kg'.format(y))
print('O menor peso lido foi:{:.2f}Kg'.format(z))