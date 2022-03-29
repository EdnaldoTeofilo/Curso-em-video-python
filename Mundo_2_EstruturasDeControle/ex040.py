#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
#Média abaixo de 5.0:Reprovado-----Média entre 5.0 e 6.9:Recuperação-----Média 7.0 ou superior:Aprovado
x = float(input('Digite a sua primeira nota:'))
y = float(input('Digite a sua segunda nota: '))
m = (x+y)/2
print ('Sua média foi de: {:.1f}'.format(m))
if m < 5:
    print('Você foi REPROVADO!')
elif m >= 7:
    print('Você foi aprovado PARABêNS!')
elif 5 <= m <7:
    print('Você ficou de RECUPERAÇÃO!')