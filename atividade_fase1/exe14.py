#Programa que calcula o gasto com aluguel de um carro.

dia = float(input('Quantos dias contradados de aluguel ? '))
km_contatada = float(input('Qual a km contratada ? '))
km_usada = float(input('Qual a km usada ? '))

preco_dia = dia * 60

if km_usada < km_contatada:
    km_devolvida = (km_contatada - km_usada)*0.15
    km_usada = (km_usada * 0.15) + preco_dia
    km_contrtatado = (km_contatada * 0.15) + preco_dia
    print(f'O valor do contato é R$ {km_contrtatado}')
    print(f'Você usou menos que o serviço contratado em Km no valor de R$ {km_usada} .')
    print(f'Será extornado o valor de R$ {km_devolvida} referente ao valor não usado.')

elif km_usada == km_contatada:
    km_usada = (km_usada * 0.15) + preco_dia
    print(f'Você usou o limite contratado no valor de R$ {km_usada}.')

else :
    km_usada = (km_usada * 0.15) + preco_dia
    print(f'Você excedeu o limete de contrato somando o valor de R$ {km_usada}.')

    
