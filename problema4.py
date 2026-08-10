chaves_pix = {}

def cadastrar_chave():
    chave = input("Digite a chave PIX (cpf/cnpj/email/telefone): ")

    if chave in chaves_pix:
        print("Erro: essa chave PIX já está cadastrada.")
        return

    nome = input("Nome: ")
    banco = input("Banco: ")
    numero_conta = input("Número da conta: ")

    chaves_pix[chave] = {
        "nome": nome,
        "banco": banco,
        "numero_conta": numero_conta
    }
    print("Chave PIX cadastrada com sucesso!")


def consultar_chave():
    chave = input("Digite a chave PIX que deseja consultar: ")

    if chave not in chaves_pix:
        print("Erro: essa chave PIX não está cadastrada.")
        return

    dados = chaves_pix[chave]
    print(f"Nome: {dados['nome']}")
    print(f"Banco: {dados['banco']}")
    print(f"Número da conta: {dados['numero_conta']}")


def menu():
    while True:
        print("\n--- Sistema de Chaves PIX ---")
        print("1 - Cadastrar chave")
        print("2 - Consultar chave")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_chave()
        elif opcao == "2":
            consultar_chave()
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
