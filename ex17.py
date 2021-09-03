'''17. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.'''

import random
n1 = input('digite um nome :')
n2 = input('digite um nome:')
n3 = input('digite um nome:')
n4 = input('digite um numero')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)
print(' O aluno escolhido foi {}'.format(escolhido))

