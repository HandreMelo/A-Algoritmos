############## Manipular a entrada de string ###############

grafo_teste_1=[]
texto = "'A','B','C','D'"
j=0
for i in range(len(texto)):
    if texto[i]!="'" and texto[i]!=",":
        grafo_teste_1.append(texto[i])
        
print(grafo_teste_1)
for i in range(len(grafo_teste_1)):
    print(grafo_teste_1[i])


########### Método para tirar caracteres especiais de uma string ###########

palavra = "'A','B','C','D'"
print(palavra)
palavra1 = palavra.replace("'", "").replace(',','')
print(palavra1)
grafo_teste_2 = {}
grafo_teste_2[palavra1[0]] = [palavra1[1], palavra1[2]]
print(grafo_teste_2)


############## LER ARQUIVO 1 ##############

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


################ LER ARQUIVO 2 #############

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

   
########## LER ARQUIVO, MANIPULAR STRING E CONSTRUIR GRAFO #############

vetor_ler = []
arquivo_destino = open('grafo.txt', 'r')
for linha in arquivo_destino:
    vetor_ler.append(linha.strip())
    

print(vetor_ler)
arquivo_destino.close()

for i in range(len(vetor_ler)):
    vetor_ler[i] = vetor_ler[i].replace("'", "").replace(',','')
print(vetor_ler)
grafo = {}

n = int(vetor_ler[0])
adjacentes=[]
pesos=[]
for i in range(n):
    for j in range(n):
        if vetor_ler[i+2][j] != '0':
           adjacentes.append(vetor_ler[1][j])
           pesos.append(vetor_ler[i+2][j])
    grafo[vetor_ler[1][i]] = [adjacentes,pesos]
    adjacentes=[]
    pesos=[]
print(grafo)
