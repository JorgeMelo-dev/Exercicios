def dividir(num1, num2):
    #try:
    return num1 / num2
    #except ZeroDivisionError:
    #    return "Não é possível dividir por zero."
    #except ValueError:
    #    return "Entrada inválida. Por favor, insira números inteiros."
    #else:
    #    return "Divisão realizada com sucesso."
    #finally:
    #    print("Operação de divisão concluída.")


# Programa principal
try:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado_divisao = dividir(num1, num2)
    print(f"O resultado da divisão de {num1} / {num2} = {resultado_divisao}")
except ZeroDivisionError:
    print("Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.")
except ValueError:
    print("Entrada inválida. Por favor, insira números inteiros.")  
else:
    print("Divisão realizada com sucesso.")
finally:
    print("Operação de divisão concluída.\n")
