natureza = ["rio", "floresta", "leão", "montanha", "oceano", "estrela", "vento", "cachoeira", "lua", "girassol"]

tecnologia = ["algoritmo", "API", "blockchain", "código", "software", "nuvem", "hardware", "interface", "pixel", "servidor"]

def retornar_listas(natureza,tecnologia):
    soma_lista = natureza + tecnologia
    return soma_lista

juntando_lista = retornar_listas(natureza,tecnologia)
print(f'A lista junta: {juntando_lista}')

