# 7- Sistema de restaurante (valores baseados em media dos restaurantes)
cardapio = {
    1: {"nome": "Salada Italiana", "preco": 44.0},
    2: {"nome": "Espaguete", "preco": 165.0},
    3: {"nome": "Churros com Doce de Leite Argentino", "preco": 40.0},
    4: {"nome": "Suco", "preco": 12.9}
}

def mostrar_cardapio(cardapio):
    print("Cardápio:")
    for chave, item in cardapio.items():
        print(f"{chave}. {item['nome']} - R${item['preco']:.2f}")

def fazer_pedido(cardapio):
    total = 0
    while True:
        mostrar_cardapio(cardapio)
        opcao_str = input("Digite o número do prato (0 para finalizar): ")
        if opcao_str.isdigit():
            opcao = int(opcao_str)
            if 0 <= opcao <= len(cardapio):
                if opcao == 0:
                    break
                item = cardapio[opcao]
                total += item['preco']
                print(f"Você escolheu {item['nome']}")
            else:
                print("Opção inválida.")
        else:
            print("Por favor, digite um número válido.")

    return total

def pagamento(total):
    while True:
        valor_pago_str = input("Digite o valor pago: ")
        if valor_pago_str.replace(".", "").isdigit():
            valor_pago = float(valor_pago_str)
            if valor_pago >= total:
                troco = valor_pago - total
                print(f"Troco: R${troco:.2f}")
                break
            else:
                print("Valor insuficiente.")
        else:
            print("Por favor, digite um valor numérico válido.")

total_pedido = fazer_pedido(cardapio)
print(f"Valor total do pedido: R${total_pedido:.2f}")
pagamento(total_pedido)