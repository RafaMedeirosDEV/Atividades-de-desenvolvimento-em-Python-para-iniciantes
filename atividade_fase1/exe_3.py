# Lendo o que o usuário escrever e mostrando sobre ele

palavra= input('Digite algo: ')

print(f'A Palavra digitada foi : {palavra}')
print(f'A palavra é Alfabetica ou numerica ? {palavra.isalnum()}')
print(f'A palavra contem apenas letra Maiúscula ? {palavra.isupper()}')
print(F'A palavra tem apenas letra Minúscila ? {palavra.islower()}')


