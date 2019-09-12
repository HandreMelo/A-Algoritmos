package br.com.grafos;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.lang.reflect.Array;
import java.util.*;

public class GraphLogic {

    public void lerListaGrafo(){
        String csvArquivo = "/Users/Phelipe Hass/IdeaProjects/arquivo.txt";
        BufferedReader conteudoCsv = null;
        String linha="";
        String csvSeparador = ",";
        String[] armazena = {};
        List<String[]> dados = new ArrayList<String[]>();
        try {
            conteudoCsv = new BufferedReader(new FileReader(csvArquivo));
            while((linha = conteudoCsv.readLine())!=null){

                armazena = linha.split(csvSeparador);
                dados.add(armazena);

            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        }
        encontraCaminho(dados);

    }

    private void encontraCaminho(List<String[]> grafo){
        List<List<String>> mapaCaminho = new ArrayList<List<String>>();
        List<String> dadosMapa = new ArrayList<>();
        int x=0,y=0;
        for(x=0;x<3;x++){

            for(y=0;y<grafo.size()-1;y++){
                dadosMapa.add(x==0 ? grafo.get(x)[y] : "999999999");
            }
            mapaCaminho.add(dadosMapa);
            dadosMapa = new ArrayList<>();
        }
        mapaCaminho.get(1).set(0,"0");

        //aqui ja comeca a percorrer para achar o caminho com A como raiz
        for(x=0;x<grafo.size();x++){ //entender se 'X' começa em 0 ou 1

            for(y=1;y<grafo.size();y++){
                int tempo = Integer.parseInt(grafo.get(y)[x]);
                if(tempo>0){
                    String vertAdj = grafo.get(0)[y-1];
                    if(Integer.parseInt(mapaCaminho.get(y).get(1))>tempo){ //aqui da treta
                        mapaCaminho.get(y-1).set(1,String.valueOf(tempo));
                        mapaCaminho.get(y).set(1,grafo.get(x)[0]);
                    }
                }
            }
        }
    }

}
