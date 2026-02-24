valor_minimo_do_desconto = 100.00
taxa_desconto =0.10

def exibir_menu_usuario():
    """Exibir o menu principal da calculadora"""
    print('\n---Calculadora de Carrinho---')
    print("1. Adicionar preço de Produtos")
    print("2. Ver Carrinho e calcular Total")
    print("3. Esvaziar carrinho")
    print("4. Sair")

def adicionar_preco(carrinho):
    #Vetor 
    """Adiciona um novo preço ao Vetor 'carrinho' """
    try:
        #Manipulação de tipos de dados (str --> float)
        preco_str = input("Digite o preço do produto (ex:19.99)")
        preco = float(preco_str)

        if preco > 0:
            carrinho.append(preco) #append ele está colocando o preço dentro do carrinho
            print(f"Produto de R$ {preco:.2f} adicionado.")
        else:
            print(f"O preço deve ser um valor positivo")

    except ValueError:
        print("Erro, valor inválido. Digite um número")

def ver_carrinho_e_total(carrinho):
    """Calcule e exibe o subtotal, desconto e total a pagar"""

    if not carrinho:
        print("Seu carrinho está vazio")
        return #termina a função mais cedo

    print('\n --- Itens no Carrinho ---')
    subtotal =  0.0 #tem que atribuir um valor

    for preco in carrinho:
        print(f"R$ {preco:.2f}")
        subtotal = subtotal + preco

    print(f"\nSubtotal: R$ {subtotal:.2f}")
    total_a_pagar = subtotal

    if subtotal > valor_minimo_do_desconto:
        desconto = subtotal * taxa_desconto
        total_a_pagar = subtotal - desconto
        print(f"Desconto (10%): R$ {desconto:.2f}")

    else:
        print("Nenhum desconto aplicado (compra acima de R$ 100.00)")

    print(f"Total a pagar: R$ {total_a_pagar:.2f}")

def esvaziar_carrinho(carrinho):
    carrinho.clear()
    print("Carrinho esvaziado com sucesso")

def main_carrinho():  #o main vai ser o que vai ser chamado primeiro
    carrinho_de_compras = []

    while True:
        exibir_menu_usuario()
        opcao = input("Escolha uma opção (1-4): ")

        if opcao == '1':
            adicionar_preco(carrinho_de_compras)
        elif opcao == '2':
            ver_carrinho_e_total(carrinho_de_compras)
        elif opcao == '3':
            esvaziar_carrinho(carrinho_de_compras)
        elif opcao == '4':
            print("Saindo do Sistema de carrinho...")
            break #Encerra o laço 'while'
        else:
            print("Opção inválida!")

main_carrinho()
