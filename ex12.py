'''12. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
area = larg x altura
tinta = area/'''

largura = float(input('Qual a largura da parade?'))
altura = float(input('Qual a altura?'))

area = largura * altura
tinta = area/2

print(' A area da sua parede é de {}m² e para pintar voce vai precisar de {} litros de tintas'.format(area, tinta))