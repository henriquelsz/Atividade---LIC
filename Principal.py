import nomeComida as nc

resultado = -1
while resultado == -1:
    n = input('Digite a comida/bebida que deseja: ').lower()
    resultado = nc.comida(n)
    if resultado != -1:
        print('O preço do(a) {} é {}R$'.format(n, resultado))
