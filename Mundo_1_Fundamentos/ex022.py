#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas. O nome com todas minúsculas.
#Quantas letras ao todo(sem considerar espaços). Quantas letras tem o primeiro nome.
x = str(input('Digite seu nome completo:')).strip() #.strip para remoção de espaços antes e dps do que é escrito
 
print ('Seu nome maiuscula é: {}'.format(x.upper()))
print ('Seu nome minusculo é: {}'.format(x.lower()))
print ('Seu nome tem {} letras'.format(len(x) - x.count(' ')))
#print ('Seu primeiro  nome tem {} letras.'.format(x.find(' '))) #Ele acha o primeiro espaço e diz a posição, como a contagem começa em 0 não precisa mudar o valor da posição
separa = x.split() #Separa pelo os espaços
print ('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0],len(separa[0])))