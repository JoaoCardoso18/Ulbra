altura = float(input('Forneça a altura do cilindro: '))
raio = float(input('Forneça o raio do cilindro: '))
pi = float(3.14)

areabase = pi * (raio*raio)
arealateral = 2 * pi * altura
areatotal = areabase * arealateral

litros = areatotal / 15
valor = ((litros * 150),2)
latas_necessarias = litros / 10
print ('Você precisará de {} que resulta em {} litros'.format(latas_necessarias, litros))