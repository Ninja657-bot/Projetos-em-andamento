import os

#Lista vazia para começar
lista_vendas = []

#Funções usadas no programa
def realizar_venda():  #Realiza a venda de um produto
    os.system("cls")
    item = input("Digite o nome do produto: ")
    quant = int(input("Digite a quantidade: "))
    valor = float(input("Digite o valor do produto: R$"))
    print()
    
    venda = {"produto": item, "quantidade": quant, "preco": valor} 
    
    print("Produto registrado com sucesso! ")
    return venda

def valor_total():  #Calcula o valor total de vendas
    total = 0
    
    for venda in lista_vendas:
        total += venda["quantidade"] * venda["preco"]
    
    return total 

def total_vendas():  #Calcula o total de vendas realizadas
    return len (lista_vendas)

def produto_mais_vendido():  #Verifica qual foi o produto mais vendido
    totais = {}

    for venda in lista_vendas:
        produto = venda["produto"]
        quantidade = venda["quantidade"]

        if produto in totais:
            totais[produto] += quantidade
        else:
            totais[produto] = quantidade
    
    maior = max(totais.values())
    for produto, quantidade in totais.items():
        if quantidade == maior:
            return produto

def relatorio():  #Gera o relatório com todas as vendas
    #Chamada das funções
    valor = valor_total()
    total = total_vendas()
    produto_max = produto_mais_vendido()
    total_produtos = 0  #Variável para contar os produtos vendidos
    
    #Interface do relatório
    print(f"{'Nº':<5} {'Produto':<15} {'Quantidade':<10} {'Preço':>10}")
    print("-" * 45)

    for i, venda in enumerate(lista_vendas, start=1):  #Listagem de vendas detalhadas
        print(f"{i:<5} {venda['produto']:<15} {venda['quantidade']:<10} R$ {venda['preco']:>7.2f}")
        
        total_produtos += venda["quantidade"]  #Soma todos os produtos vendidos 

    #Exibição de resultados
    print("-" * 45)
    print(f"Total de vendas: {total}")
    print(f"Total de produtos vendidos: {total_produtos}")
    print(f"Valor total arrecadado: R$ {valor:.2f}")
    print(f"O produto mais vendido foi: {produto_max}")
    
#Início da Interface
while True:
    os.system("cls")
    print("-" * 19, "SVG 1.0", "-" * 19)
    print()
    print("Bem vindo ao Sistema de Gestão de Vendas! (SGV)")
    print()
    menu = int(input("""1 | Registrar venda
2 | Gerar Relatório
3 | Encerrar programa
"""))
    #Opções do sistema 
    match menu:
        #Adiciona venda ao sistema
        case 1:
            lista_vendas.append(realizar_venda())
            continue
        
        #Gerar relatório
        case 2:
            #Não executa o relatório caso não haja produtos cadastrados 
            if not lista_vendas:
                os.system("cls")
                print("Você ainda não possui vendas cadastradas!")
                input("Pressione ENTER para voltar ao menu")
                continue
            
            #Geração de relatório
            relatorio()
            print()
            
            #Verifica se o usuário deseja encerrar o sistema
            print("Deseja Encerrar o Sistema ?")
            fim = (input("""S - Sim  N - Não
""")).upper()
            if fim == "S":
                exit()
            else:
                continue
        
        #Fecha o sistema
        case 3:
            exit()
