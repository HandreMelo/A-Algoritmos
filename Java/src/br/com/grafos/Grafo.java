package br.com.grafos;

public class Grafo {
    private String vertice;
    private String verticeAdj;
    private Integer peso;

    public Grafo(String vertice, String verticeAdj, Integer peso) {
        this.vertice = vertice;
        this.verticeAdj = verticeAdj;
        this.peso = peso;
    }

    public String getVertice() { return vertice; }

    public String getVerticeAdj() { return verticeAdj; }

    public Integer getPeso() { return peso; }

    public void setVertice(String vertice) {
        this.vertice = vertice;
    }

    public void setVerticeAdj(String verticeAdj) {
        this.verticeAdj = verticeAdj;
    }

    public void setPeso(Integer peso) {
        this.peso = peso;
    }


}
