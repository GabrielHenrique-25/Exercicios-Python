numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def mostrar_media(numeros):
    media = sum(numeros) / len(numeros)
    print(f'A média do valor informado foi: {media:.2f}')

mostrar_media(numeros)