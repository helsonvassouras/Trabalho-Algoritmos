clientes = []

def adicionar_cliente(nome, email, telefone, endereco):
    cliente = [nome, email, telefone, endereco]
    clientes.append(cliente)
    print(f"\nCliente {nome} adicionado com sucesso!")

def exibir_clientes():
    if not clientes:
        print("\nNenhum cliente cadastrado.")
    else:
        print("\nLista de Clientes:")
        for i, cliente in enumerate(clientes, 1):
            print(f"{i}. Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")

def buscar_cliente(email):
    for cliente in clientes:
        if cliente[1] == email:
            print(f"\nCliente encontrado: Nome: {cliente[0]}, E-mail: {cliente[1]}, Telefone: {cliente[2]}, Endereço: {cliente[3]}")
            return cliente
    print("\nCliente não encontrado.")
    return None

def remover_cliente(email):
    cliente = buscar_cliente(email)
    if cliente:
        clientes.remove(cliente)
        print(f"\nCliente com o e-mail {email} removido com sucesso!")
    else:
        print(f"\nNão foi possível remover o cliente com o e-mail {email} porque ele não foi encontrado.")

def main():
    while True:
        print("\nSistema de Cadastro de Clientes da ExpertDEVS:")
        print("1. Adicionar Cliente")
        print("2. Exibir Clientes")
        print("3. Buscar Cliente por E-mail")
        print("4. Remover Cliente")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            nome = input("Nome: ")
            email = input("E-mail: ")
            telefone = input("Telefone: ")
            endereco = input("Endereço: ")
            adicionar_cliente(nome, email, telefone, endereco)
        elif opcao == "2":
            exibir_clientes()
        elif opcao == "3":
            email = input("Digite o e-mail do cliente: ")
            buscar_cliente(email)
        elif opcao == "4":
            email = input("Digite o e-mail do cliente a ser removido: ")
            remover_cliente(email)
        elif opcao == "5":
            print("\nSaindo do sistema...")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
