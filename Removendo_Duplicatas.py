numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def remover_duplicatas_preservando_ordem(lista):
    unica = []
    vistos = set()
    for num in lista:
        if num not in vistos:
            unica.append(num)
            vistos.add(num)
    return unica

print(remover_duplicatas_preservando_ordem(numeros))
