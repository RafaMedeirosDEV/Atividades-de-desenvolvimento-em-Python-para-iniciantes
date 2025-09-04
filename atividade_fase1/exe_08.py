#convertendo medidas de centimetros em metros e milimetros

metro = float(input('Digite a medida que deseja converter.\nObs.: não use a (,) caso necessário use o ponto para fazer a separação:'))

centimetro = metro*100
milimetro = centimetro*100

print(f'A Medida de {metro} convertida para metros é: {centimetro} cm\nconvertida em milímetros é: {int(milimetro)} mm')

