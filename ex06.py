def cadastrarPessoa():
    try:
        nome = input("Digite o nome da pessoa: ")
        idade = int(input("Digite a idade da pessoa: "))    
        
        if not nome:
            raise ValueError("O nome não pode ser vazio.")
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
    except ValueError as e:
        print(f"Erro ao cadastrar pessoa: {e}")
    else:
        print(f"Pessoa cadastrada com sucesso: {nome}, {idade} anos.")  
    finally:
        print("Operação de cadastro concluída.\n")  

# Programa principal
cadastrarPessoa()
