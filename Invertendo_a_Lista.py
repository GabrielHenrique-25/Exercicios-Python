from time import sleep
numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3,
           42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]


def mostrar_normal_inverso(numeros):
    normal = sorted(numeros)
    inverso = sorted(numeros,reverse=True)
    print(f'Os números em ordem crescente: {normal}')
    print()
    print('Reformulando...')
    print()
    sleep(1)
    print(f'Os numeros em ordem decrescente: {inverso}')

mostrar_normal_inverso(numeros)
