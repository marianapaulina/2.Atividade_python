'''16. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15
por Km rodado.'''

km = float(input('quantos km voce pecorreu com o carro ?'))
dias = int(input('por quantos dias voce alugou o carro? '))
print('voce deve pagar R${}'.format(dias*60 + km*0.15))

