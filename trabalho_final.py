# Constantes da lista
ENERGIA = 'Energia em kcal'
TAMANHO = 'Tamanho da folha em metros'
NOMEC = 'Nome cientifíco da planta'
NOMEP = 'Nome popular da planta'

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
        NOMEP: 'jambú',
        NOMEC: 'acmella oleracea',
        ENERGIA: 32,
        TAMANHO: 0.045
    },

    {
        NOMEP: 'taperebá',
        NOMEC: 'spondias mombin',
        ENERGIA: 40,
        TAMANHO: 0.06
    },

    {
        NOMEP: 'tucumã',
        NOMEC: 'astrocaryum aculeatum',
        ENERGIA: 474,
        TAMANHO: 0.10
    },
    {
        NOMEP: 'açaí',
        NOMEC: 'euterpe oleracea',
        ENERGIA: 60,
        TAMANHO: 200.5
    }
            ]

def cabecalho() -> None:
    print(f"{'-':-^50}")
    print(f"{CORES['verde']}{' LISTA DE PANCS ':-^50}{CORES['limpar']}")
    print(f"{'-':-^50}")

def menu() -> None:
        """
        Irá mostrar o menu na tela
        """
        cabecalho()
        print(f"-----{' 1. Visualizar lista completa ':-<45}")
        print(f"-----{' 2. Visualizar um item da lista ':-<45}")
        print(f"-----{' 3. Visualizar um trecho da lista ':-<45}")
        print(f"-----{' 4. Inserir novo item na lista ':-<45}")
        print(f"-----{' 5. Sair ':-<45}")
        print(f"{'-':-^50}")

def buscar_item(indice_busca: int) -> None:
    """
    Mostrará um item em específico da lista
    
    Argumentos:
        indice_busca: posição do item desejado
    """
    print(f"{'-':-^50}")
    print(f"{CORES['ciano']}{indice_busca+1}{CORES['limpar']} {NOMEP}: {CORES['roxo']}{lista_pancs[indice_busca][NOMEP]}{CORES['limpar']}")
    print(f" {NOMEC}: {CORES['amarelo']}{lista_pancs[indice_busca][NOMEC]}{CORES['limpar']}")
    print(f" {ENERGIA}: {CORES['verde']}{lista_pancs[indice_busca][ENERGIA]}{CORES['limpar']}")
    print(f" {TAMANHO}: {CORES['azul']}{lista_pancs[indice_busca][TAMANHO]}{CORES['limpar']}")
    print(f"{'-':-^50}")

def lista_completa(final: int) -> None:
    """
    Irá mostrar a lista completa das pancs
    
    Argumentos:
        final: total de itens da lista
    """
    print(f"{CORES['verde']}{' LISTA DE PANCS ':-^50}{CORES['limpar']}")
    for i in range (0, final):
        buscar_item(i)

def mensagemErro(texto: str) -> None:
    """
    Mostrará uma mensagem com coloração vermelha para o erro
    
    Argumentos:
        texto: Texto que deseja exibir
    """
    print(f'{CORES['vermelho']}{texto}{CORES['limpar']}')

def mensagemAviso(texto: str) -> None:
    """
    Mostrará uma mensagem com coloração azulada para o aviso
    
    Argumentos:
        texto: Texto que deseja exibir
    """
    print(f'{CORES['ciano']}{texto}{CORES['limpar']}')

def inputColorido(texto: str, cor: str = 'amarelo') -> str:
    """
    Irá mostrar a mensagem do input de forma colorida
        
    Argumentos:
        texto: Texto que deseja exibir
        cor: Cor a qual deseja exibir o texto, por padrão é amarelo

    Retorno:
        Retorna a string inserida pelo usuário
    """
    print(f'{CORES[cor]}{texto}{CORES["limpar"]}', end='')
    mensagem = input()
    return mensagem


executar = True
while executar:
    final = len(lista_pancs)
    menu()
    opcao = str(inputColorido("Digite uma opção: "))

    if opcao == '1':
        lista_completa(final)
    
    # Opção de buscar item específico
    elif opcao == "2":
        cabecalho()
        print(f"-----{f' 1. Busca por índice ':-<45}")
        print(f"-----{' 2. Busca por nome popular ':-<45}")
        print(f"{'-':-^50}")
        busca = str(inputColorido("Você deseja fazer uma busca por índice ou por nome? (1 ou 2) "))
        if busca == '1': # Busca por índice
            try:
                indice_busca = int(inputColorido("Qual o índice do item que você deseja visualizar? "))
                if indice_busca > final:
                    mensagemAviso(f"Opção inválida. A lista possui apenas {final} itens")
                else:
                    buscar_item(indice_busca - 1)
            except ValueError:
                mensagemErro("Opção não é um índice")
            
            except:
                mensagemErro("Houve um erro no valor digitado")

        elif busca == '2': # Busca por nome
            nome_busca = str(inputColorido("Qual o nome popular da planta que você deseja visualizar? ")).lower()
            encontrada = False
            for i in range(0,final):
                if lista_pancs[i][NOMEP].lower() == nome_busca:
                    buscar_item(i)
                    encontrada = True
            if not encontrada:
                mensagemAviso("Planta não encontrada")
        
        else:
            mensagemErro("Opção inválida")
        
    # Buscar intervalo
    elif opcao == '3':
        valido = False
        while not valido: # Irá validar as respostas
            try:
                inicio = int(inputColorido("Digite o índice do item inicial do trecho: "))
            except ValueError:
                mensagemErro("O valor digitado não é um índice")
                continue
            try:
                fim = int(inputColorido("Digite o índice do item final do trecho: "))
                valido = True
            except ValueError:
                mensagemErro("O valor digitado não é um índice")
                continue

        if inicio < 1 or inicio > final or fim > final:
            mensagemErro("Intervalo inválido")

        else:
            print(f"{' LISTA DE PANCS ':-^50}")
            for i in range (inicio-1,fim):
                buscar_item(i)
            
    # Adicionar itens a lista
    elif opcao == '4':
        if final==50:
            mensagemAviso("Não é possível adicionar mais itens à lista")

        else:
            nomep_novo_item = str(inputColorido('Qual o nome popular da planta (str)? ' )).lower()
            nomec_novo_item = str(inputColorido(f'Qual o nome científico da planta (str)? ')).lower()
            valido = False
            while not valido: # Teste de validade das respostas
                try:
                    energia_novo_item = int(inputColorido('Qual o valor energético em Kcal da planta (int)? '))
                    if energia_novo_item < 0:
                        energia_novo_item *= -1
                except ValueError:
                    mensagemErro("Não é um valor energético válido")
                    continue
                except:
                    mensagemErro("Houve um erro no valor digitado")
                    continue

                try:
                    tamanho_novo_item = float(inputColorido('Qual o TAMANHO médio das folhas dessa planta? (float) '))
                    if tamanho_novo_item < 0:
                        tamanho_novo_item *= -1
                    valido = True
                except ValueError:
                    mensagemErro("Não é um valor de TAMANHO de folhas válido")
                    continue
                except:
                    mensagemErro("Houve um erro no valor digitado")
                    continue

            novo_item = {
                NOMEP: nomep_novo_item,
                NOMEC: nomec_novo_item,
                ENERGIA: energia_novo_item,
                TAMANHO: tamanho_novo_item
                }
                    
            lista_pancs.append(novo_item)
            final += 1
            lista_completa(final)

    # Finalizar programa
    elif opcao == '5':
        print(f"{CORES['azul']}Obrigado por usar o nosso Software :){CORES['limpar']}")
        executar = False

    # Opção que não seja de 1 a 5
    else:
        mensagemErro("Opção inválida. Digite um valor válido (1, 2, 3, 4 ou 5)")
