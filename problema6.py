notas = {
    'Joao': 8.5,
    'Maria': 9.0,
    'Pedro': 7.8,
    'Ana': 9.5
}

aluno_maior_nota = None
maior_nota = None

for nome, nota in notas.items():
    if maior_nota is None or nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = nome

print(f"O aluno com a maior nota é {aluno_maior_nota}, com nota {maior_nota}")

