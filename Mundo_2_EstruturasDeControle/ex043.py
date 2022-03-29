#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do Peso   -Entre 18.5 e 25: Peso ideal   - 25 até 30: Sobrepeso      - 30 até 40: obesidade     - Acima de 40: Obesidade mórbida 

p = float(input('Digite o seu peso em kilogramas: '))
a = float(input('Digite sua altura em metros:'))
i = p/(a*a)
if i < 18.5:
    print('Você está abaixo do peso!')
elif 18.5 <= i < 25:
    print('Você está no peso ideal!')
elif 25 <= i < 30:
    print('Você está com sobrepeso!')
elif 30 <= i < 40:
    print('Você está com obesidade!')
elif i >= 40:
    print('Você está com obesidade mórbida!')
