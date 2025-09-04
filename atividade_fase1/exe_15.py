#Programa que transforma um número fracionado em inteiro eliminando o o que estiver depois da vígula, usando a função trunc()

from math import trunc

num = float(input('Digite um  número fracionado usando a vírgulo como separador:'))
num_int = trunc(num)

print(f'O número escolhido foi {num } o número interiro dele é {num_int}')

