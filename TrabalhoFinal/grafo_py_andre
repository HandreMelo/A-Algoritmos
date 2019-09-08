def calcular_grau(chave):
   return len(grafo[chave][0])


def mostrar_conjunto():
   print(grafo)


def mostrar_caminho(dicionario):
   for key, value in dicionario.items():
       print(key, value)

#dicionario = grafo
def depth_dirst_search(dicionario, inicio, fim):
    #aqui é o tal TRAVA no primeiro
   print(dicionario[inicio])
   pilha = [(inicio, [inicio])]

   #for key, value in test_dict.items(): 
   #print (key, value) 

   while pilha:
        #o *vertice é um único valor e *caminho uma lista de vertices...
        #...extraídos de *pilha, por isso,while pilha, porque ela tende a ficar vazia
       vertice, caminho = pilha.pop()
    #dicionario[vertice][0] - caminho, segue a lista até não haver Não repetidos
    #o set(dicionario[v][0] - set(caminho) esta testando se esse vertice ja nao existe na lista caminho.
       for proximo in set(dicionario[vertice][0]) - set(caminho):
           if proximo == fim:
               yield caminho + [proximo]
           else:
            #e aqui, enquanto não achar, adiciona na pilha quem vai ser o proximo a ser analisado e..
            #...já colocando como caminho passado
               pilha.append((proximo, caminho + [proximo]))

#A set is an unordered collection with no duplicate elements. 
#Basic uses include membership testing and eliminating duplicate entries.


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


#grafo = {'A': [['B', 'C'], ['1', '9']], 'B': [['C'], ['3']], 'C': [[], []]}
#grafo = {'A': [['H', 'C'], ['1', '1']], 'B': [['D', 'F'], ['2', '3']], 'C': [['B', 'F'], ['1', '20']], 'D': [['F', 'G'], ['4', '7']], 'E': [[], []], 'F': [['G'], ['2']], 'G': [['E'], ['1']], 'H': [[], []]}
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
       print(grafo.values()) 

   elif argument == '4':
       mostrar_caminho(grafo)

   elif argument == '5': 
       inicio_vertice = input('Diga qual o vértice de início: ')
       fim_vertice = input('Diga qual o vértice de saída: ')
       caminhos = list(depth_dirst_search(grafo, inicio_vertice, fim_vertice))
       if caminhos:  # Se a lista não estiver vazia
           print('Todos os possíveos caminhos: ', caminhos)
           print('teste : ')
           peso_vvk=0
           peso_antes=999999
           for i in range(len(caminhos)):
               #print(len(caminhos))
               print('Caminho no : ' + str(i))
               for j in range(len(caminhos[i])-1):
                   vertice_key = caminhos[i][j] #um vertice 'A':
                   adjacente_vk = caminhos[i][j+1]
                   valores_vk = grafo[vertice_key] #valores desse vertice 'A': -> [['B','C']['1','2']]
                   indice_adj = valores_vk[0].index(adjacente_vk)
                   print('>'+valores_vk[1][indice_adj])
                   peso_vvk += int(valores_vk[1][indice_adj])
               if peso_vvk<peso_antes:
                   #print(peso_vvk)
                   peso_antes=peso_vvk
                   peso_vvk=0
           print('Menor peso : ' + str(peso_antes))       
       else:
           print('Este caminho não é possível')
   else:
       print('Valor incorreto')

# https://pt.stackoverflow.com/questions/67593/grafo-caminhos-poss%C3%ADveis-python
# algoritmo de dijkstra
