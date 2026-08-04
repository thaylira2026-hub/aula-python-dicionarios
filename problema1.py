string = "Samanta"
string = string.lower()
contagem = {}

for letra in string:
    if letra in contagem:
        contagem[letra] += 1
    else:
        contagem[letra] = 1

for letra in sorted(contagem):
    print(f"{letra}: {contagem[letra]}")
    