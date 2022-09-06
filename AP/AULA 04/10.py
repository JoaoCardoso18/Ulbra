nome = input('O nome do vendedor é ')
sf = float(input('Qual o salário fixo do vendedor: '))
cv = int(input('Quantos carro esse vendedor vende por mês '))
vc = float(input('Quanto ele recebe por carro '))

s = sf + cv * (cv * 1.15)

print('O salário do vendedor {} é de {}'.format(nome, s))


