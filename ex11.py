'''11. Faça um programa que insira um valor em reais, e faça ele converter o valor para dólar, mostrando quantos
#dólares podem ser comprados com aquela quantia. (Valor para ser usado do dólar no exercício: 5.30)'''

real =  float(input('insira um valor em reais:R$'))
dolar = real/5.30
print(' Voce pode comprar {:.2f} dólares com esse valor'.format(dolar))