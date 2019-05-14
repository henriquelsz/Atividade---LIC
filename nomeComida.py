def comida(nome):
    if nome == 'dadinho':
        preco = 0.50
        return preco
    elif nome == 'bolo':
        preco = 4.50
        return preco
    elif nome == 'capuccino':
        preco = 6.00
        return preco
    elif nome == 'cafe':
        preco = 4.00
        return preco
    elif nome == 'sorvete':
        preco = 6.00
        return preco
    elif nome == 'suco':
        preco = 5.00
        return preco
    elif nome == 'refrigerante':
        preco = 4.50
        return preco
    elif nome == 'salgado':
        preco = 4.00
        return preco
    else:
        print('Nome do salgado é invalido, digite novamente...')
        return -1
