objetos = [{'nome': 'Gabriel'}, {'nome': 'Bruno'}, {'nome': 'Maria'}]

def buscar_nomes(objetos):
    nomes = []
    for obj in objetos:
        nomes.append(obj['nome'])
    return nomes

print(buscar_nomes(objetos))