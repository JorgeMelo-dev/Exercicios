def ler_inteiro():
    num = int(input("Digite um número inteiro: "))
    return num


# Programa principal
try:
    numero = ler_inteiro()
    print(f"O número digitado foi: {numero}")  
except ValueError:
    print("Entrada inválida. Por favor, insira um número inteiro.")
else:
    print("Número lido com sucesso.")
finally:    
    print("Operação de leitura concluída.\n")   

