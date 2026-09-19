import os
import time
os.system("cls")

#Variaveis
alunos = {}
notas = []
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
2| Mostrar Média dos alunos"""))
    match escolha:
        case 1:
            while True:
                #limpar terminal
                os.system("cls")
                
                #Caso lista esteja vazia
                if not alunos:
                    print("Ainda não possuem alunos cadastrados")
                    escolha = input("Deseja adicionar alunos ? S/N ").upper()
                    if escolha == "S": 
                        os.system("cls")
                        print("Prosseguindo para cadastramento de aluno")
                        time.sleep(2)
                        os.system("cls")
                        
                        #Cadastro do nome
                        nome = input("Digite o nome do aluno: ")
                        
                        #cadastro da nota
                        for i in range (4):
                            nota = float(input(f"Digite a {i+1}ª do aluno:"))
                            notas.append(nota)
                        
                        alunos[nome] = notas
                        
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
                        
                        
                        
                    
                    