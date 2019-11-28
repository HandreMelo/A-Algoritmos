var i,
    N = 100,
    E = 500,
    s = new sigma(),
    cam = s.addCamera();

// Generate a random graph:
var grafo = document.getElementById('grafo').innerHTML;
var graphJs = JSON.parse(grafo);
for(var chave in graphJs){
    s.graph.addNode({id: chave,label: 'Vertice '+chave,x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
}
var i = 1;
for(var chave in graphJs){
    for(var adj in graphJs[chave]){
        i++;
        s.graph.addEdge({id: 'e'+i,source: chave,target: adj,size: 1 + Math.random()});
    }

}
//s.graph.addNode({id: 'A',label: 'Vertice A',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//s.graph.addNode({id: 'B',label: 'Vertice B',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//s.graph.addNode({id: 'C',label: 'Vertice C',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//s.graph.addNode({id: 'D',label: 'Vertice D',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//s.graph.addNode({id: 'E',label: 'Vertice E',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//s.graph.addNode({id: 'F',label: 'Vertice F',x: Math.random(),y: Math.random(),size: 4 + (3 * Math.random()) | 0 });
//
//s.graph.addEdge({id: 'e1',source: 'A',target: 'B',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e2',source: 'B',target: 'C',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e3',source: 'C',target: 'D',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e4',source: 'D',target: 'A',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e5',source: 'F',target: 'B',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e6',source: 'F',target: 'C',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e7',source: 'E',target: 'A',size: 1 + Math.random()});
//s.graph.addEdge({id: 'e8',source: 'E',target: 'C',size: 1 + Math.random()});

// Instantiate sigma:
s.addRenderer({
  container: document.getElementById('svg'),
  type: 'svg',
  settings: {
    hideEdgesOnMove: true,
    defaultLabelColor: '#fff',
    defaultNodeColor: 'yellow',
    defaultEdgeColor: 'blue',
    edgeColor: 'default'
  }
});

s.addRenderer({
  container: document.getElementById('canvas'),
  type: 'canvas',
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