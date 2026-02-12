def calculaMedia(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
                 

# Programa principal
try:
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media_final = calculaMedia(nota1, nota2)
    print(f"A média final é: {media_final}")    
except ValueError:
    print("Entrada inválida. Por favor, insira números válidos para as notas.") 
else:    
    print("Média calculada com sucesso.")
finally:    
    print("Operação de cálculo da média concluída.\n")  
