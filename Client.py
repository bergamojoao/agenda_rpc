import xmlrpc.client

server = xmlrpc.client.ServerProxy("http://localhost:8080")

op = 1
while op != 0:
    op = int(input("1 - Adicionar um contato\n2 - Consultar contatos\n3 - Alterar contato\n4 - Remover Contato\n0 - Sair\nSelecione uma opção: "))
    if op == 1:
        try:
            name = input("Digite o nome: ")
            address = input("Digite o endereço: ")
            phone = input("Digite o telefone: ")
            server.inserir(name, address, phone)
        except Exception as ex:
            print("ERRO INESPERADO!!! ", str(ex))
    elif op == 2:
        try:
            name = input("Digite o nome do contato: ")
            people = server.consultar(name)
            print("\nResultados encontrados para: \"%s\""%(name,))
            print("ID\tNOME\tEND.\tTEL.")
            for person in people:
                print("%d\t%s\t%s\t%s"%(person['_Person__id'], person['_Person__name'], person['_Person__address'], person['_Person__phone']))
            print("")
        except Exception as ex:
            print("ERRO INESPERADO!!! ", str(ex))
    elif op == 3:
        try:
            id = int(input("\nDigite o ID do contato que deseja alterar: "))
            old_person = server.consultar_id(id)
            opt = input("Deseja alterar nome? S/N > ")
            if opt == "S" or opt == "s":
                print("Nome Antigo: " + old_person['_Person__name'])
                nome = input("Digite o novo nome: ")
            else: nome = old_person['_Person__name']

            opt = input("Deseja alterar o endereço? S/N > ")
            if opt == "S" or opt == "s":
                print("Endereço Antigo: " + old_person['_Person__address'])
                endereco = input("Digite o novo endereço: ")
            else: endereco = old_person['_Person__address']

            opt = input("Deseja alterar o telefone? S/N > ")
            if opt == "S" or opt == "s":
                print("Telefone Antigo: " + old_person['_Person__phone'])
                telefone = input("Digite o novo telefone: ")
            else: telefone = old_person['_Person__phone']

            server.alterar(id, nome, endereco, telefone)
            print("Contato alterado com sucesso!\n")
        except Exception as ex:
            print("ERRO INESPERADO!!! ", str(ex))
    elif op == 4:
        try:
            id = int(input("\nDigite o ID do contato que deseja remover: "))
            server.remover(id)
            print("Contato removido com sucesso!\n")
        except Exception as ex:
            print("ERRO INESPERADO!!! ", str(ex))