def funcao1():
    print('Teste de transposição')


if __name__ == '__main__':
    funcao1()
    print('primeiro.py está sendo executado diretamente')
else:
    print(f'primeiro.py foi importado {__name__}')