# Constantes
energia = 'Energia em kcal'
tamanho = 'Tamanho da folha em metros'
nomec = 'Nome cientifíco da planta'
nomep = 'Nome popular da planta'

# Adicionando cores
CORES = {
    "limpar": "\033[m",
    "vermelho": "\033[31m",
    "amarelo": "\033[33m",
    "azul": "\033[34m",
    "roxo": "\033[35m",
    "verde": "\033[32m",
    "ciano": "\033[36m"
}

lista_pancs = [
     {
        nomep: 'jambú',
        nomec: 'acmella oleracea',
        energia: 32,
        tamanho: 0.045
    },

    {
        nomep: 'taperebá',
        nomec: 'spondias mombin',
        energia: 40,
        tamanho: 0.06
    },

    {
        nomep: 'tucumã',
        nomec: 'astrocaryum aculeatum',
        energia: 474,
        tamanho: 0.10
    },
    {
        nomep: 'açaí',
        nomec: 'euterpe oleracea',
        energia: 60,
        tamanho: 200.5
    }
            ]

def menu() -> None:
        """
        Irá mostrar o menu na tela
        """
        print(f"{'-':-^50}")
        print(f"{' LISTA DE PANCS ':-^50}")
        print(f"{'-':-^50}")
        print(f"-----{' 1. Visualizar lista completa ':-<45}")
        print(f"-----{' 2. Visualizar um item da lista ':-<45}")
        print(f"-----{' 3. Visualizar um trecho da lista ':-<45}")
        print(f"-----{' 4. Inserir novo item na lista ':-<45}")
        print(f"-----{' 5. Sair ':-<45}")
        print(f"{'-':-^50}")

def lista_completa(final: int) -> None:
    """
    Irá mostrar a lista completa das pancs
    """
    print(f"{CORES['amarelo']}{' LISTA DE PANCS ':-^50}{CORES['limpar']}")
    for i in range (0, final):
        print(f"{'-':-^50}")
        print(f"{CORES['ciano']}{i+1}{CORES['limpar']} {nomep}: {CORES['roxo']}{lista_pancs[i][nomep]}{CORES['limpar']}")
        print(f" {nomec}: {lista_pancs[i][nomec]}")
        print(f" {energia}: {lista_pancs[i][energia]}")
        print(f" {tamanho}: {lista_pancs[i][tamanho]}")
        print(f"{'-':-^50}")

def mensagemErro(erro_text: str) -> None:
    print(f'{CORES['vermelho']}{erro_text}{CORES['limpar']}')

executar = True
while executar:
    final = len(lista_pancs)
    menu()
    opcao = str(input("Digite uma opção: "))

    if opcao == '1':
        lista_completa(final)
            

    elif opcao == "2":
        print(f"{'-':-^50}")
        print(f"{' LISTA DE PANCS ':-^50}")
        print(f"{'-':-^50}")
        print(f"-----{' 1. Busca por índice ':-<45}")
        print(f"-----{' 2. Busca por nome popular ':-<45}")
        print(f"{'-':-^50}")
        busca = str(input("Você deseja fazer uma busca por índice ou por nome? (1 ou 2) "))
        if busca == '1':
            try:
                indice_busca = int(input("Qual o índice do item que você deseja visualizar? "))
                if indice_busca > final:
                    mensagemErro(f"Opção inválida. A lista possui apenas {final} itens")
                else:
                    print(f"{'-':-^50}")
                    print(f"{indice_busca} {nomep}: {lista_pancs[indice_busca-1][nomep]}")
                    print(f" {nomec}: {lista_pancs[indice_busca-1][nomec]}")
                    print(f" {energia}: {lista_pancs[indice_busca-1][energia]}")
                    print(f" {tamanho}: {lista_pancs[indice_busca-1][tamanho]}")
                    print(f"{'-':-^50}")
            except ValueError:
                mensagemErro("Opção não é um índice")
            
            except:
                mensagemErro("Houve um erro no valor digitado")

        elif busca == '2':
            nome_busca = str(input("Qual o nome popular da planta que você deseja visualizar? ")).lower()
            encontrada = False
            for i in range(0,final):
                if lista_pancs[i][nomep].lower() == nome_busca:
                    print(f"{'-':-^50}")
                    print(f"{i+1} {nomep}: {lista_pancs[i][nomep]}")
                    print(f" {nomec}: {lista_pancs[i][nomec]}")
                    print(f" {energia}: {lista_pancs[i][energia]}")
                    print(f" {tamanho}: {lista_pancs[i][tamanho]}")
                    print(f"{'-':-^50}")
                    encontrada = True
            if not encontrada:
                print("Planta não encontrada")
        
        else:
            mensagemErro("Opção inválida")
            
    elif opcao == '3':
        try:
            inicio = int(input("Digite o índice do item inicial do trecho: "))
        except ValueError:
            mensagemErro("O valor digitado não é um índice")
            continue
        try:
            fim = int(input("Digite o índice do item final do trecho: "))
        except ValueError:
            mensagemErro("O valor digitado não é um índice")
            continue

        if inicio < 1 or inicio > final or fim > final:
            mensagemErro("Intervalo inválido")

        else:
            print(f"{' LISTA DE PANCS ':-^50}")
            for i in range (inicio-1,fim):
                print(f"{'-':-^50}")
                print(f"{i+1} {nomep}: {lista_pancs[i][nomep]}")
                print(f" {nomec}: {lista_pancs[i][nomec]}")
                print(f" {energia}: {lista_pancs[i][energia]}")
                print(f" {tamanho}: {lista_pancs[i][tamanho]}")
                print(f"{'-':-^50}")
            

    elif opcao == '4':
        if final==50:
            print("Não é possível adicionar mais itens à lista")

        else:
            nomep_novo_item = str(input('Qual o nome popular da planta (str)? ' )).lower()
            nomec_novo_item = str(input('Qual o nome científico da planta (str)? ')).lower()
            valido = False
            while not valido: # Teste de validade das respostas
                try:
                    energia_novo_item = int(input('Qual o valor energético em Kcal da planta (int)? '))
                    if energia_novo_item < 0:
                        energia_novo_item *= -1
                except ValueError:
                    mensagemErro("Não é um valor energético válido")
                    continue
                except:
                    mensagemErro("Houve um erro no valor digitado")
                    continue

                try:
                    tamanho_novo_item = float(input('Qual o tamanho médio das folhas dessa planta? (float) '))
                    if tamanho_novo_item < 0:
                        tamanho_novo_item *= -1
                    valido = True
                except ValueError:
                    mensagemErro("Não é um valor de tamanho de folhas válido")
                    continue
                except:
                    mensagemErro("Houve um erro no valor digitado")
                    continue

            novo_item = {
                nomep: nomep_novo_item,
                nomec: nomec_novo_item,
                energia: energia_novo_item,
                tamanho: tamanho_novo_item
                }
                    
            lista_pancs.append(novo_item)
            final += 1
            lista_completa(final)

    elif opcao == '5':
        executar = False

    else:
        mensagemErro("Opção inválida. Digite um valor válido (1, 2, 3, 4 ou 5)")
