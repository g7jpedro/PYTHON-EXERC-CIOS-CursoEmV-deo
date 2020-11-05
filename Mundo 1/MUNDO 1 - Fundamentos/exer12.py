n = float(input('Digite o valor do produto: '))
n2 = float(input('Digite a porcentagem do desconto: '))
desc = n*n2/100
tot = n-desc

print(f'O valor de des↑conto é {desc:.2f} Reais, o valor total vai ficar {tot:.2f} Reais')