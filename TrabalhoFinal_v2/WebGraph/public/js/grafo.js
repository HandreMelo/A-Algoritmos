var i,
    N = 100,
    E = 500,
    s = new sigma(),
    cam = s.addCamera();

var entrega = document.getElementById('caminho_entregado').innerHTML;
var entregaGrafo = JSON.parse(entrega);
console.table(entregaGrafo);

var grafo = document.getElementById('grafo').innerHTML;
var graphJs = JSON.parse(grafo);
for(var chave in graphJs){
    s.graph.addNode({id: chave,label: 'Vertice '+chave,x: Math.random(),
                        y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
}
var i = 1;
for(var chave in entregaGrafo){
    for(var indice = 0; indice < entregaGrafo[chave].length-1;indice++){
        i++;
        var avanco = parseInt(indice, 10)+1;
        s.graph.addEdge({id: 'e'+i,source: entregaGrafo[chave][indice],
                        target: entregaGrafo[chave][String(avanco)],size: 1 + Math.random()});
    }
}
// Instantiate sigma:
s.addRenderer({
  container: document.getElementById('svg'),
  type: 'svg',
  camera: cam,
  settings: {
    defaultLabelColor: '#fff',
    defaultNodeColor: 'yellow',
    defaultEdgeColor: 'blue',
    edgeColor: 'default'
  }
});

s.refresh();