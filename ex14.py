'''14. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario + (salario*15/100)'''

salario = float(input('qual o seu salario ?'))
aumento = salario * 15/100
print(' o seu salario com o aumento de 15% é {}'.format( salario + aumento))
