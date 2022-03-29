'''Dentro do pacote utilidadesCeV que criamos no ex111, temos um módulo chamado dado. Crie uma função chamada leiaDinhiero() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários.'''

from utilidadescev import dado
from utilidadescev import moeda

valor = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(valor, 80, 30)