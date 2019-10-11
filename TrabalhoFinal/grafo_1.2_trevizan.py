import copy
import math


def calcular_grau(chave):
    return len(grafo[chave][0])


def mostrar_conjunto():
    print(grafo)


def mostrar_caminho(dicionario):
    for key, value in dicionario.items():
        print(key, value)


def depth_dirst_search(dicionario, inicio, fim):
    pilha = [(inicio, [inicio])]
    while pilha:
        vertice, caminho = pilha.pop()
        for proximo in set(dicionario[vertice][0]) - set(caminho):
            if proximo == fim:
                yield caminho + [proximo]
            else:
                pilha.append((proximo, caminho + [proximo]))


def sair():
    return ""


def criar_vertices(lista):
    for x in range(len(lista)):
        if not lista[x] in grafo:
            for key in lista[x]:
                grafo[key] = [[], []]


def criar_arestas(no_1, no_2, peso):
    if no_1 in grafo and no_2 in grafo:
        grafo[no_1][0] += no_2
        grafo[no_1][1] += peso
    else:
        print('Não existe vértices declarados para ligar este caminho')


def menor_caminho(grafo, inicio, fim):
    estimativa = {}  # Dicionário com a estimativa de todas as distâncias
    precedente = {}  # Dicionário com os vértices que precedem o vértice atual

    for vertice in grafo:
        estimativa[vertice] = math.inf  # Infinito
        precedente[vertice] = None

    estimativa[inicio] = 0  # Atribuimos a estimativa 0 ao vértice de partida

    S = []  # Conjunto com todos os vértices que já contém a estimativa de custo mínimo
    Q = copy.copy(grafo)  # Conjunto que contém os demais vértices (Q = Vertices - S)

    vertice = None
    menor_estimativa = None

    for temp_vertice in Q:
        if vertice is None:
            vertice = temp_vertice
            menor_estimativa = estimativa[temp_vertice]
    print(grafo)
    print(estimativa)
    print(precedente)
    print(S)
    print(Q)
    print(menor_estimativa)


def ler_arquivo():
    grafo_destino = {}
    arquivo_destino = open('destino.txt', 'r')

    for vertice in arquivo_destino:
        linha = vertice.strip()
        grafo_destino.update({linha[0]: [linha[2], linha[4]]})
        print(linha)

    print(grafo_destino)
    arquivo_destino.close()

    arquivo_entregas = open('entregas.txt', 'r')
    arquivo_entregas.close()

    return ''


# grafo = {}
dic = {}
grafo = {'A': [['B', 'D'], ['1', '2']],
         'B': [['A', 'C', 'D'], ['1', '1', '2']],
         'C': [['B', 'D'], ['1', '3']],
         'D': [['A', 'B', 'C'], ['2', '2', '3']]}
lista_vertices = []

while (True):
    ler_arquivo()
    print('Digite 1: Adicionar vértices e Arestas')
    print('Digite 2: Calcular o grau de um dado vértice')
    print('Digite 3: Mostrar os conjuntos de vértices e arestas')
    print('Digite 4: Responder se um vértice é alcançável diretamente a partir de outro')
    print('Digite 5: Depth Dirst Search:')
    print('Digite 0: Sair')
    argument = input()

    if argument == '0':
        print('Programa Finalizado')
        break

    elif argument == '1':
        print('Adicione os vértices (em maiúsculo): ')
        while (True):
            elemento = input()
            if elemento == '0':
                break
            else:
                lista_vertices.append(elemento)
        criar_vertices(lista_vertices)

        print('Adicione as arestas (em maiúsculo), para sair 0 e 0: ')
        while True:
            aresta_x = input('De: ')
            aresta_y = input('Para: ')
            if aresta_x == '0' or aresta_y == '0':
                break
            else:
                valor = input('Peso: ')
                criar_arestas(aresta_x, aresta_y, valor)

    elif argument == '2':
        maior_grau = max(grafo, key=calcular_grau)
        print(maior_grau)
        print(grafo[maior_grau][0])

    elif argument == '3':
        mostrar_conjunto()

    elif argument == '4':
        # mostrar_caminho(grafo)
        menor_caminho(grafo, 'A', 'C')

    elif argument == '5':
        inicio_vertice = input('Diga qual o vértice de início: ')
        fim_vertice = input('Diga qual o vértice de saída: ')
        caminhos = list(depth_dirst_search(grafo, inicio_vertice, fim_vertice))
        if caminhos:  # Se a lista não estiver vazia
            print('Todos os possíveos caminhos: ', caminhos)
            print('Caminho mais curto: ', min(caminhos, key=len))
        else:
            print('Este caminho não é possível')
    else:
        print('Valor incorreto')

# https://pt.stackoverflow.com/questions/67593/grafo-caminhos-poss%C3%ADveis-python --> depth dirst search
# https://medium.com/@random.wicket/%C3%A1rvores-de-caminhos-%C3%B3timos-em-grafos-e-o-problema-da-classifica%C3%A7%C3%A3o-supervisionada-b34c9465552b --> Dijkstra menor caminho
# http://prorum.com/?qa=2482/resolver-problema-caminho-usando-tecnica-first-branch-bound --> First Branch + Bound
# https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/ --> Minimum spanning tree
# https://github.com/andrewalker/grafos/blob/master/Dijkstra.py --> Dijkstra
