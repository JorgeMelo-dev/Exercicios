def calculaIMC():
    try:
        peso = float(input("Digite seu peso em kg: "))
        altura = float(input("Digite sua altura em metros: "))
        imc = peso / (altura ** 2)
    except ValueError:
        print("Entrada inválida. Por favor, insira números válidos para peso e altura.")
    except ZeroDivisionError:
        print("Altura não pode ser zero. Por favor, insira uma altura válida.")
    else:
        print(f"Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Classificação: Abaixo do peso")
        elif 18.5 <= imc < 25:
            print("Classificação: Peso normal") 
        elif 25 <= imc < 30:
            print("Classificação: Sobrepeso")       
        else:
            print("Classificação: Obesidade")   
    finally:
        print("Operação de cálculo do IMC concluída.\n")    


# Programa principal        
calculaIMC()
