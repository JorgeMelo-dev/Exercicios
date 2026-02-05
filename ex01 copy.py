continuar = "s"

while continuar == "s":
    print("\nEscolha uma opção:")
    print("1 - Verificar se um numero é par ou impar")
    print("2 - verifique o número")
    print("3 - calcular o dobro de um valor")

    opcao = int(input("\nDigite a opção desejada: "))
    match opcao:
        case 1:
            print(" 1 - par ou ímpar")
            numero = int(input("Escolha um número:"))
            if numero %2 == 0:
                print("O numero é par.")
            else:
                print("o numero é impar.") 
        case 2:
            print(" 2 - Verifique o número")
            numero1 = int(input("Escolha o 1º número:"))
            numero2 = int(input("Escolha o 2º número:"))
            if numero1 > numero2:   
                print(f"{numero1} é maior.")
            elif numero1 < numero2:
                print(f"{numero2} é maior.")
            else:
                print ("Os números são iguais.")
        case 3:
            print(" 3 - Dobro")
            n = int(input("Escolha o 1° numero: ")) 
            print(f"O dobro do número é: {n*2}") 
        case _:
            print('Opção inválida')      

    # strip() => remove todos os espaços
    continuar = input("\nDeseja continuar? (s/n): ").strip().lower()

    if continuar != "s":
        print("Programa encerrado!\n")
        break

