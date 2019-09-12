package br.com.grafos;

public class VerticeAdj {
    private String verticeAdj;
    private Integer peso;



    public VerticeAdj(String verticeAdj, Integer peso) {
        this.verticeAdj = verticeAdj;
        this.peso = peso;
    }

    public String getVerticeAdj(){ return this.verticeAdj; }

    public Integer getPeso(){ return this.peso; }

    public void setVerticeAdj(String verticeAdj){ this.verticeAdj = verticeAdj; }

    public void setPeso(Integer peso){ this.peso = peso; }
}
