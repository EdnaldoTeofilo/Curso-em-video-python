'''Faça um programa que leia a largura e a altura de uma parede em metros,
   calcule a sua área e a quantidade de tinta necessária para pintá-la, 
   sabendo que cada litro de tinta, pinta uma área de 2m².'''
    
alt = int(input('Qual altura da parede em metros? '))
larg = int(input('Qual largura da parede em metros? '))
área = alt*larg 
print (f'Área da parede é de {área} m².')
tinta = área / 2
print (f'E precisará de {tinta}l de tinta para pintar a parede.')