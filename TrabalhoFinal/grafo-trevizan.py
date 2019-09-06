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
               grafo[key] = [[],[]]


def criar_arestas(no_1, no_2, peso):
   if no_1 in grafo and no_2 in grafo:
       grafo[no_1][0] += no_2
       grafo[no_1][1] += peso
   else:
       print('Não existe vértices declarados para ligar este caminho')


grafo = {}
lista_vertices = []

while (True):
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
       mostrar_caminho(grafo)

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

# https://pt.stackoverflow.com/questions/67593/grafo-caminhos-poss%C3%ADveis-python
# algoritmo de dijkstra

