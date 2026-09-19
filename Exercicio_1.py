import os
import time
os.system("cls")

#Variaveis
alunos = {}
nomes = str
nota = float
media = float

#Controladores do loop
voltar = False

while True:
    os.system("cls")
    print("- Cauculadora de Médias -")#Agora na Unifacs
    print()

    escolha = int(input("""1| Ver alunos da lista
2| Mostrar Média dos alunos
"""))
    match escolha:
        case 1:
            while True:
                #limpar terminal
                os.system("cls")
                
                #Caso lista esteja vazia
                if not alunos:
                    print("Ainda não possuem alunos cadastrados")
                    escolha = input("""Deseja adicionar alunos ? S/N 
""").upper()
                    if escolha == "S": 
                        os.system("cls")
                        print("Prosseguindo para cadastramento de aluno")
                        time.sleep(2)
                        os.system("cls")
                        
                        #Cadastro do nome
                        nome = input("Digite o nome do aluno: ")
                        
                        #cadastro da nota
                        notas = []
                        
                        for i in range (3):
                            nota = float(input(f"Digite a nota da {i+1}ª unidade: "))
                            notas.append(nota)

                        alunos[nome] = notas
                        
                        print()
                        print("Notas cadastradas com sucesso!")
                        print()
                        input ("Presione ENTER para continuar")
                        continue
                    
                    elif escolha == "N":
                        os.system("cls")
                        print("Retornando ao menu principal")
                        time.sleep(2)
                        break
                    
                    else:
                        os.system("cls")
                        print("Opção inválida")
                        print("Tente novamente")
                        time.sleep(2.5)
                        continue
                    
                for i, (nome, notas) in enumerate (alunos.items(), start=1):
                    print(f"\nAluno {i}")
                    print(f"Nome do Aluno: {nome}")
                    for unidade, nota in enumerate(notas, start=1):
                        print(f"{unidade}ª Unidade: {nota}")
                        print()
                        
                cadastro = int(input("""1 | Adicionar Aluno
2 | Remover Aluno
3 | Voltar ao Menu
    """))
                
                match cadastro:
                    case 1:
                        os.system("cls")
                        #Cadastro do nome
                        nome = input("Digite o nome do aluno: ")
                        
                        #cadastro da nota
                        notas = []
                        
                        for i in range (3):
                            nota = float(input(f"Digite a nota da {i+1}ª unidade: "))
                            notas.append(nota)
                        
                        alunos[nome] = notas
                        
                        print()
                        print("Notas cadastradas com sucesso!")
                        print()
                        input ("Presione ENTER para continuar")
                        continue
                     
                    case 2:
                        os.system("cls")
                        
                        print("===== Remover aluno =====")
                        print()
                        
                        for i, nome in enumerate(alunos, start=1):
                            print(f"{i} - {nome}")
                            print()
                        
                        aluno_remover = int(input("Aluno a ser removido: "))
                        
                        nomes = list(alunos.keys())
                        
                        
                        if 1 <= aluno_remover <= len(nomes):
                            
                            nome_remover = nomes[aluno_remover - 1]
                            del alunos[nome_remover]
                            print()
                            
                            print(f"Removido com sucesso!")
                            print()
                            input("Pressione ENTER para continuar")
                            continue
                        else:
                            print("Opção invalida tente novamente")
                            print()
                            input("Pressione ENTER para prosseguir")
                            continue
                        
                    case 3:
                        os.system("cls")
                        print("Voltando ao menu principal")
                        print()
                        input("Presione ENTER para prosseguir")
                        break
        
        case 2:
            if not alunos:
                os.system("cls")
                print("Ainda não possuem alunos cadastrados")
                print()
                input("Pressione ENTER para prosseguir")
                continue
                
            #Mostrar alunos novamente
            for i, (nome, notas) in enumerate (alunos.items(), start=1):
                print(f"\nAluno {i}")
                print(f"Nome do Aluno: {nome}")
                for unidade, nota in enumerate(notas, start=1):
                    print(f"{unidade}ª Unidade: {nota}")
            
            #Calculos
                soma = sum(notas)
                media = soma /3
                print(f"Soma das notas: {soma}")
                print(f"Média do aluno(a): {media}")
            #Verificação de desempenho
                if media < 7:
                    status = "Reprovado"
                if media >= 7:
                    status = "Aprovado"
                print(f"Status: {status}")  
                exit()  
