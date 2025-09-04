#calculando o valor de um salário acrescentando 15% para aumento.

salario = float(input('Valor do Salário atual R$ '))
porcentagem = float(input('Valor da procentagem a reajustar :'))

aumento = (salario*porcentagem)/100

novo_salario = salario+aumento

print(f'O salário atual é R$ {salario}, com o aumento de {porcentagem:.2f} % será reajustado para R$ {novo_salario:.2f}.')