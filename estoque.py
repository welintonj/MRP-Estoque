import sys

produtos = {}   # Estrutura: { id: {"nome":..., "categoria":..., "preco":..., "quantidade":...} }
contador_id = 1

def cadastrar_produto():
    global contador_id

    print("\n📦 CADASTRO DE PRODUTO")
    nome = input("Nome: ")
    categoria = input("Categoria: ")
    preco = float(input("Preço: R$ "))
    quantidade = int(input("Quantidade inicial: "))

    produtos[contador_id] = {
        "nome": nome,
        "categoria": categoria,
        "preco": preco,
        "quantidade": quantidade
    }

    print(f"\n✔ Produto cadastrado com ID: {contador_id}")
    contador_id += 1


def excluir_produto():
    print("\n🗑 EXCLUSÃO DE PRODUTO")
    try:
        id_produto = int(input("Informe o ID do produto a excluir: "))
        if id_produto in produtos:
            del produtos[id_produto]
            print("✔ Produto excluído com sucesso!")
        else:
            print("❌ ID não encontrado.")
    except:
        print("❌ Entrada inválida.")


def movimentar_estoque():
    print("\n🔄 MOVIMENTAÇÃO DE ESTOQUE")
    try:
        id_produto = int(input("ID do produto: "))
        if id_produto not in produtos:
            print("❌ Produto não encontrado.")
            return
        
        print("\n1 - Entrada de estoque")
        print("2 - Saída de estoque")
        opc = input("Escolha a operação: ")

        qtd = int(input("Quantidade: "))

        if opc == "1":
            produtos[id_produto]["quantidade"] += qtd
            print("✔ Entrada registrada.")
        elif opc == "2":
            if produtos[id_produto]["quantidade"] >= qtd:
                produtos[id_produto]["quantidade"] -= qtd
                print("✔ Saída registrada.")
            else:
                print("❌ Estoque insuficiente.")
        else:
            print("❌ Opção inválida.")
    except:
        print("❌ Entrada inválida.")


def listar_produtos():
    print("\n📋 RELATÓRIO DE PRODUTOS")
    
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    
    for idp, dados in produtos.items():
        alerta = " ⚠ ESTOQUE BAIXO!" if dados["quantidade"] < 5 else ""
        print(f"""
ID: {idp}
Nome: {dados["nome"]}
Categoria: {dados["categoria"]}
Preço: R$ {dados["preco"]:.2f}
Quantidade: {dados["quantidade"]}{alerta}
        """)


def menu():
    while True:
        print("\n==== MINI ERP DE ESTOQUE ====")
        print("1 - Cadastrar produto")
        print("2 - Excluir produto")
        print("3 - Movimentar estoque (entrada/saída)")
        print("4 - Relatório de produtos")
        print("5 - Sair")
        
        opc = input("Escolha uma opção: ")

        if opc == "1":
            cadastrar_produto()
        elif opc == "2":
            excluir_produto()
        elif opc == "3":
            movimentar_estoque()
        elif opc == "4":
            listar_produtos()
        elif opc == "5":
            print("\nEncerrando o sistema... Até mais!")
            sys.exit()
        else:
            print("❌ Opção inválida.")


menu()