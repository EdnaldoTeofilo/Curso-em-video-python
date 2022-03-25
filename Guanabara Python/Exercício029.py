#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar RR$7,00 por cada Km acima do limite.
x = int(input('Qual a velocidade atual do carro? '))
y = (x-80)*7
if x>80:
    print ('MULTADO! Você excedeu o limite permitido que é de 80Km/h \n Você deve pagar uma multa de R${:.2f}'.format(y))
print ('Tenha um bom dia! Dirija com segurança!')