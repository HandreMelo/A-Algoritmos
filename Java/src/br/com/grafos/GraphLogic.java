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
                dadosMapa.add(x==0 ? grafo.get(x)[y].toString() : "999999999");
            }
            mapaCaminho.add(dadosMapa);
        }
        mapaCaminho.get(0).get(1).replace(mapaCaminho.get(0).get(1).toString(),"0");

        //aqui ja comeca a percorrer para achar o menor caminho com A como raiz
        for(x=0;x<grafo.size();x++){ //entender se 'X' começa em 0 ou 1

            for(y=1;y<grafo.size();y++){
                if(!grafo.get(x)[y].equals(0)){
                    int tempo =  Integer.parseInt(grafo.get(x)[y]);
                    String vertAdj = grafo.get(y-1)[0];
                    if(Integer.parseInt(mapaCaminho.get(y-1).get(1))>tempo){
                        mapaCaminho.get(y-1).get(1)
                                .replace(mapaCaminho.get(y-1).get(1).toString(),String.valueOf(tempo));
                        mapaCaminho.get(y-1).get(2)
                                .replace(mapaCaminho.get(y-1).get(2).toString(),grafo.get(x)[0]);
                    }
                }
            }
        }
    }




}
