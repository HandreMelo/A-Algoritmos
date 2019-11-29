var i,
    N = 100,
    E = 500,
    s = new sigma(),
    cam = s.addCamera();

var grafo = document.getElementById('grafo').innerHTML;
var graphJs = JSON.parse(grafo);
for(var chave in graphJs){
    s.graph.addNode({id: chave,label: 'Vertice '+chave,x: Math.random(),
                        y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
}
var i = 1;
for(var chave in graphJs){
    for(var adj in graphJs[chave]){
        i++;
        s.graph.addEdge({id: 'e'+i,source: chave,target: adj,size: 1 + Math.random()});
    }
}

s.addRenderer({
  container: document.getElementById('canvas'),
  type: 'canvas',
  camera: cam,
  settings: {
    batchEdgesDrawing: true,
    hideEdgesOnMove: true,
    defaultLabelColor: '#3D3F41',
    defaultNodeColor: 'blue',
    defaultEdgeColor: 'yellow',
    edgeColor: 'default'
  }
});

s.refresh();