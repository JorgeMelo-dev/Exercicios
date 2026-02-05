quant = int(input("Escolha a quantidade de testes: "))
quant = quant + 1;

nota = -1
soma = 0
i = 1
while i < quant:
    while nota < 0 or nota > 10:
        nota = float(input(f"Digite a nota-{i}: "))
    
    soma = soma + nota
    i = i + 1
    nota = -1 
media = soma / (i-1)     

if media >= 7:
    print(f"Média = {media:.2f} - Aluno aprovado!\n")
elif media >= 5:
    print(f"Média = {media:.2f} - Aluno em recuperação!\n")
else:
    print(f"Média = {media:.2f} - Aluno reprovado!\n")


