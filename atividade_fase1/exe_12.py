#calculando 5% de desconto.

produto = float(input('Qual o valor do produto: R$ '))

desconto = (produto*5)/100

print(f'O Valor do produto é R$ {produto:.2f}')
print(f'O valor para á vista tem 5% de desconto e será de R$ {produto-desconto}')
