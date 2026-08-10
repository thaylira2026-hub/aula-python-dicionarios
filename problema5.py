from datetime import datetime

conversas = {}

def cadastrar_mensagem():
    telefone = input("Digite o número de telefone: ")
    mensagem = input("Digite a mensagem: ")

    if telefone not in conversas:
        conversas[telefone] = []

    registro = {
        "mensagem": mensagem,
        "data_hora": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    }

    conversas[telefone].append(registro)
    print("Mensagem cadastrada com sucesso!")


def consultar_mensagens():
    telefone = input("Digite o número de telefone: ")

    if telefone not in conversas or len(conversas[telefone]) == 0:
        print("Nenhuma mensagem encontrada para esse número.")
        return

    mensagens = conversas[telefone]
    for registro in reversed(mensagens):
        print(f"[{registro['data_hora']}] {registro['mensagem']}")


def menu():
    while True:
        print("\n--- WhatsApp Simulado ---")
        print("1 - Cadastrar mensagem")
        print("2 - Consultar mensagens")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_mensagem()
        elif opcao == "2":
            consultar_mensagens()
        elif opcao == "3":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()
