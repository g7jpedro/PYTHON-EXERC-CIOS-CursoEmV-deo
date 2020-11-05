#Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas.
n = input('Digite algo: ')
print(f'É alfabético ?\n{n.isalpha()}')
print(f'É númerico ?\n{n.isnumeric()}')
print(f'É maiúsculo ?\n{n.isupper()}')
print(f'É minúsculo ?\n{n.islower()}')
