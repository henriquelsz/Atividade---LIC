import nomeComida as nc

"""
Exercicio 2
"""
nomes = []
salgados = []
precos = []
for k in range(0,7,1):
    n = input('Digite seu nome: ')
    salg = input('Digite seu pedido: ').lower()
    preco = nc.comida(salg)
    if preco != -1:
        nomes.append(n)
        salgados.append(salg)
        precos.append(preco)
        print(nomes)
        print(salgados)

print()
print(nomes)
print(salgados)

"""
Exercicio 3
"""
print()
total = 0
for k in range(0,7,1):
    print('{}\t\t{}\t  {}R$'.format(nomes[k],salgados[k],precos[k]))
    total = total + precos[k]

print()
print('Valor total {}R$'.format(total))
