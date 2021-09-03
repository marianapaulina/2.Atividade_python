'''13. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = preço - (preço *5/100)'''

preço = float(input('qual o valor do produto?'))
desconto = preço * 5/100
print('o seu produto com um desconto de 5% ficarar no valor de {}'.format( preço - desconto))
