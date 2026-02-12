def calculadora(op, num1, num2):
    match op:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2
        case _:
            return "Operação inválida. Por favor, escolha uma operação válida (+, -, *, /)."


# Programa principal
resp = "S"

while resp.upper() == "S":
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        op = input("Digite a operação desejada (+, -, *, /): ")

        resultado = calculadora(op, num1, num2)
        print(f"O resultado da operação {num1} {op} {num2} é: {resultado}") 
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos.")
    except ZeroDivisionError:
        print("Não é possível dividir por zero. Por favor, insira um divisor diferente de zero.")    
    else:    
        print("Operação realizada com sucesso.")
    finally:
        resp = input("\nDeseja realizar outra operação? (S/N): ")

    if resp.upper() != "S":
        print("Encerrando a calculadora. Obrigado por usar!\n")   
        break
    