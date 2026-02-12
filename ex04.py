def buscarAluno(nome):
    alunos = {"Ana": 8.5, "Bruno": 9.2, "Carla": 7.8}
    aluno = alunos[nome]
    return aluno


# Programa principal
nome = input("Digite o nome do aluno que deseja buscar: ").capitalize()
try:
    nota = buscarAluno(nome)
    print(f"A nota do aluno {nome} é: {nota}")
except KeyError:
    print(f"Aluno {nome} não encontrado.")    
else:
    print("Aluno encontrado com sucesso.")  
finally:
    print("Operação de busca concluída.\n") 

