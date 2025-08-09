numeros = [987654321, 2, 7654321, 56, 1234567, 1, 88888, 3, 42, 999999, 5, 1000000000, 13, 101010, 7, 444, 9, 2, 13, 9]

def procurar(numero, lista):
    for item in lista:
        if item == numero:
            return True
    return False

print(procurar(56, numeros)) 
print(procurar(10003, numeros))