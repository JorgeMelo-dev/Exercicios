def consultaProduto():
    produtos = {
        "001": {"nome": "Camiseta", "preco": 29.99},
        "002": {"nome": "Calça Jeans", "preco": 79.99},
        "003": {"nome": "Tênis Esportivo", "preco": 149.99}
    }
    
    try:
        codigo_produto = input("Digite o código do produto (ex: 001, 002, 003): ")
        qtde = int(input("Digite a quantidade desejada: "))

        if qtde <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")

        produto = produtos[codigo_produto]
        valorTotal = produto['preco'] * qtde
        print(f"Produto: {produto['nome']}, Preço: R${produto['preco']:.2f}")
        print(f"Quantidade: {qtde}")
        print(f"Total: R${valorTotal:.2f}")
    except KeyError:
        print("Código de produto inválido. Por favor, tente novamente.")
    except ValueError:
        print("Quantidade inválida. Por favor, insira uma quantidade válida.")
    finally:
        print("Consulta de produto concluída.\n")

# Programa principal
consultaProduto()
