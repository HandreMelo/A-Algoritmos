package br.com.grafos;

import java.util.ArrayList;
import java.util.List;

public class Vertice {
    private String vertice;
    //private List<String> listVertAdj = new ArrayList<>();
    private List<VerticeAdj> verticesAdjs = new ArrayList<>();

    public Vertice(String vertice, List<VerticeAdj> verticeAdjs){
        this.vertice = vertice;
        this.verticesAdjs =verticeAdjs;
    }

    public String getVertice(){ return this.vertice; }

    public void setVertice(String vertice){ this.vertice = vertice; }

    public List<VerticeAdj> getVerticesAdjs(List<VerticeAdj> verticeAdjs){
        return this.verticesAdjs;
    }

    public void setVerticesAdjs(List<VerticeAdj> verticesAdjs){
        this.verticesAdjs = verticesAdjs;
    }

    public void addListaVerticeAdj(String vertAdj, Integer peso){
        VerticeAdj verticeAdjac = new VerticeAdj(vertAdj,peso);
        this.verticesAdjs.add(verticeAdjac);
    }
}

