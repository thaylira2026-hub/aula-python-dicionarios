def inverter_dicionario(dicionario):
    dicionario_invertido = {}
    for chave, valor in dicionario.items():
        if valor in dicionario_invertido:
            
            if isinstance(dicionario_invertido[valor], list):
                dicionario_invertido[valor].append(chave)
            else:
                dicionario_invertido[valor] = [dicionario_invertido[valor], chave]
        else:
            dicionario_invertido[valor] = chave
    return dicionario_invertido



palavras = {
    "house": "casa",
    "dog": "cachorro",
    "book": "livro",
    "home": "casa"   
}

resultado = inverter_dicionario(palavras)
print(resultado)

# Saída:
# {'casa': ['house', 'home'], 'cachorro': 'dog', 'livro': 'book'}