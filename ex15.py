'''15. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
farenheit é ((9*celsius)/5)+32'''

celsius = int(input('digite uma temparatura em graus celsius:'))
farenheit = ((9*celsius)/5)+32

print('{} graus celsius é {} farenheit'. format(celsius, farenheit))