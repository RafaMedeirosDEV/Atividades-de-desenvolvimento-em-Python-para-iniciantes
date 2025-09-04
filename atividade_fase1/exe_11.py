#Programa que sugere a quantidade de tinta é necessária para pintar uma parede sugerida pelo usuário.

Altura = float(input('Digite a altura da parede: '))
largura =  float(input('Digite a largura da parede: '))

parede = Altura*largura

total = parede/2

print(f'A quantidade de tinta para pintar {parede}m² é de {total} latas de tinta .')