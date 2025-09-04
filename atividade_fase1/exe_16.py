#calculando a hipotenusa, sendo um o comentaário dele usando apenas recursos nativos

'''
co = float(input('Medida do Cateto Oposto: '))
ca = float(input('Medida do Cateto Adjacente: '))
hi = (co**2 + ca**2)**(1/2)

print(f'O cateto oposto é {co}, o cateto adjacente é {ca}, sendo a hiponusa {hi:.2f}.')
'''

from math import hypot

co = float(input('Medida do Cateto Oposto: '))
ca = float(input('Medida do Cateto Adjacente: '))
hi = hypot(co,ca)
print(f'A Hipotenusa é : {hi:.2f}.')



