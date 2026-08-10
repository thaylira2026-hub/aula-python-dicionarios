turma = {}

avaliacoes_validas = ["CP1", "CP2", "CP3", "Sprint 1", "Sprint 2", "GS"]


def adicionar_aluno():
    rm = input("Digite o RM do aluno: ")

    if rm in turma:
        print("Erro: já existe um aluno cadastrado com esse RM.")
        return

    nome = input("Digite o nome do aluno: ")

    notas = {"nome": nome}
    for avaliacao in avaliacoes_validas:
        nota = float(input(f"Digite a nota de {avaliacao}: "))
        notas[avaliacao] = nota

    turma[rm] = notas
    print("Aluno cadastrado com sucesso!")


def alterar_nota():
    rm = input("Digite o RM do aluno: ")

    if rm not in turma:
        print("Erro: não existe aluno cadastrado com esse RM.")
        return

    avaliacao = input("Digite a avaliação que deseja alterar (CP1, CP2, CP3, Sprint 1, Sprint 2, GS): ")

    if avaliacao not in avaliacoes_validas:
        print("Erro: avaliação inválida.")
        return

    nova_nota = float(input("Digite a nova nota: "))
    turma[rm][avaliacao] = nova_nota
    print("Nota alterada com sucesso!")


def calcular_media_semestral():
    for rm, dados in turma.items():
        soma = sum(dados[avaliacao] for avaliacao in avaliacoes_validas)
        media = soma / len(avaliacoes_validas)
        dados["MS"] = media
        print(f"Aluno {dados['nome']} (RM {rm}) - Média Semestral: {media:.2f}")


def menu():
    while True:
        print("\n--- Sistema de Turma ---")
        print("1 - Adicionar aluno")
        print("2 - Alterar nota")
        print("3 - Calcular média semestral de todos os alunos")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_aluno()
        elif opcao == "2":
            alterar_nota()
        elif opcao == "3":
            calcular_media_semestral()
        elif opcao == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
