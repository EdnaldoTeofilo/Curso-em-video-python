'''Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos ex107, ex108, ex109 e ex110 para o primeiro pacote e mantenha tudo funcionando.'''

from utilidadescev import moeda

valor = float(input('Digite o preço: R$ '))
moeda.resumo(valor, 80, 30) 