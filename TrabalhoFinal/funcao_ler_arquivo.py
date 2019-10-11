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
