numeros = [987654321,2,7654321,56,1234567, 1, 88888,3,42,999999,5,1000000000,13,101010,7,444, 9, 2, 13, 9]

def definição_ocorrencias(numeros,valor):
    return numeros.count(valor)
quantidade = definição_ocorrencias(numeros,2)
print(f'As vezes que o número 13 aparece é : {quantidade}')