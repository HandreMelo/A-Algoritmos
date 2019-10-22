grafo = {}
entregas = {}

def ler_arquivo():
    vetor_ler = []
    arquivo_destino = open('grafo.txt', 'r')
    for linha in arquivo_destino:
        vetor_ler.append(linha.strip())

    arquivo_destino.close()

    try:
        for i in range(len(vetor_ler)):
            vetor_ler[i] = vetor_ler[i].replace("'", "").replace("‘", "").replace("’", "")

        pesos = []
        vertices = []
        ler_entregas = []

        n = int(vetor_ler[0])
        e = int(vetor_ler[n + 2])

        for i in range(2, n + 2):
            pesos.append(vetor_ler[i].split(','))
            
        # TRATA ARESTA COM VALOR NEGATIVO E ARESTAS IGUAIS COM VALOR 0
        for i in range(0, len(pesos)):
            for x in range(0, len(pesos[i])):
                if int(pesos[i][x]) < 0:
                    pesos[i][x] = str(0)
                if int(pesos[i][i]) != 0:
                    pesos[i][i] = str(0)

        for i in range(0, e):
            ler_entregas.append(vetor_ler[n + 3 + i].split(','))

        for i in range(e):
            entregas[ler_entregas[i][1]] = [ler_entregas[i][0], ler_entregas[i][2]]

        vertices.append(vetor_ler[1].split(','))
        vertices = vertices[0]
        adjacentes = []
        pesos_temp = []

        for i in range(n):
            for j in range(n):
                if pesos[i][j] != '0':
                    adjacentes.append(vertices[j])
                    pesos_temp.append(pesos[i][j])
            grafo[vertices[i]] = [adjacentes, pesos_temp]
            adjacentes = []
            pesos_temp = []
    except ValueError:
        print("valor numérico inválido")
    except IndexError:
        print("matriz do arquivo não está no tamanho correto")

#### fim - ler arquivo ####

#########MOSTRAR CAMINHO################
def mostrar_listas():
    print("----Grafo-----")
    print(grafo)
    print("---Entregas---")
    print(entregas)
    print("--------------")

#### calcular_peso ####
def calcular_peso(teste):
    peso=0
    while(len(teste)>2):
        a=teste.pop()
        v=teste[len(teste)-1]
        indice = grafo[v][0].index(a)
        peso+=int(grafo[v][1][indice])
    if(teste):
        a=teste.pop()
        v=teste[len(teste)-1]
        indice = grafo[v][0].index(a)
        peso+=int(grafo[v][1][indice])

    #print("Peso: " + str(peso))
    return(peso)

###### depth_first_searsh modificada para retornar o menor caminho ######
def depth_dirst_search(dicionario, inicio, fim):
   pilha = [ (inicio, [inicio]) ]
   #print(pilha)
   pesoTesteAntes = 99999
   pesoTeste=0
   menor_caminho=[]
   menor_peso=0
   while pilha:
       vertice, caminho = pilha.pop()
       for proximo in set(dicionario[vertice][0]) - set(caminho):
           if proximo == fim:
               #print("camnho+proximo")
               #print(caminho)
               #print(proximo)
               #print(list(caminho+[proximo]))
               pesoTeste = calcular_peso(list(caminho+[proximo]))#3
               if pesoTeste < pesoTesteAntes:
                   menor_peso=pesoTeste
                   menor_caminho = list(caminho+[proximo])
                   pesoTesteAntes=pesoTeste
               break
           else:
               pilha.append((proximo, caminho + [proximo]))
   return menor_caminho,menor_peso

# entrega exemplo
# entregas = { 'vertice':['tempo_saida','lucro_da_entrega'],...}
# entregas = {'B': ['0', '1'], 'C': ['5', '10'], 'D': ['10', '8']}
# grafo do arquivo = {'A': [['B', 'D'], ['5', '2']], 'B': [['A', 'C'], ['5', '3']],
#                    'C': [['B', 'D'], ['3', '8']], 'D': [['A', 'C'], ['2', '8']]}

######### REALIZAR ENTREGAS ############
def calcular_tempo(tentativa):
    origem = list(grafo.keys())[0]
    lucro = int(entregas[tentativa][1])
    menor_caminho, tempoIda = depth_dirst_search(grafo, origem, tentativa)#2
    menor_caminho2, tempoVolta = depth_dirst_search(grafo, tentativa, origem)
    print("Caminho Ida : " + str([tempoIda]+menor_caminho))
    if(tempoIda!=tempoVolta):
        print("Caminho Ida : " + str([tempoVolta]+menor_caminho2))
    return lucro, tempoIda+tempoVolta

def fazer_entrega():
    caminhos_lucrativos={}
    caminhos_lucrativos2={}
    entregas_keys = list(entregas.keys()) 

    try:
        for tentativa in entregas_keys:
            lucro_total = 0
            tempo_pass = 0
            caminho_lucro = []
            lucro, tempo = calcular_tempo(tentativa)#1
            tempo_pass+=tempo
            lucro_total+=lucro
            for fim in list(set(entregas_keys)-set([tentativa])): #fim é o vertice de destino na lista de entregas, exceto a origem qe já foi

                tempo_saida = int(entregas[fim][0])
                
                if ( tempo_saida >= tempo_pass):
                    lucro, tempo = calcular_tempo(fim)
                    tempo_pass+=tempo
                    lucro_total+=lucro
                    caminho_lucro += fim
            caminhos_lucrativos[tentativa]=[]
            caminhos_lucrativos[tentativa] += [lucro_total] + [tentativa] + caminho_lucro

        print("Caminhos lucrativos : ")
        print(caminhos_lucrativos)
        print("Caminho mais lucrativo: " + str(max(caminhos_lucrativos.values())))
        print()
    except ValueError:
        print("Econtrado valores inválidos no dicionário")
    except KeyError:
        print("Ocorreu um erro causado por matriz mal definida no arquivo")

######## MAIN ##############
lista_vertices = []
ler_arquivo()

def main():
    while (True):

        print('Digite 1: Mostrar o grafo e a lista de entregas')
        print('Digite 2: Fazer Entregas:')
        print('Digite 0: Sair')
        argument = input()

        if argument == '0':
            print('Programa Finalizado')
            break

        elif argument == '1':
            mostrar_listas()

        elif argument == '2':
            fazer_entrega()

        else:
            print('Valor incorreto')

if __name__ == "__main__":
    main()
