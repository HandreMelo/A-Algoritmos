package br.com.grafos;

import java.util.*;

public class Main {


    public static void main(String[] args) {
	// write your code here

        HashMap<String,HashMap<String, Integer>> testes =  new HashMap<String,HashMap<String, Integer>>();

        GraphLogic grafos = new GraphLogic();
        HashMap grafo = new HashMap();
        HashMap mapaAdj = new HashMap();
        mapaAdj.put("B",8);
        mapaAdj.put("D",2);
        grafo.put("A", mapaAdj);
        mapaAdj = new HashMap();
        mapaAdj.put("A",5);
        mapaAdj.put("C",3);
        grafo.put("B",mapaAdj);
        mapaAdj = new HashMap();
        mapaAdj.put("B",3);
        mapaAdj.put("D",8);
        grafo.put("C",mapaAdj);
        mapaAdj = new HashMap();
        mapaAdj.put("C",8);
        mapaAdj.put("A",2);
        grafo.put("D",mapaAdj);

        Scanner dado;


        while (true){
            System.out.println("---Menu---");
           // System.out.println("1 - Adicionar vertices");
            System.out.println("2 - Ler lista grafo");
            System.out.println("3 - Calcular menor caminho");
            System.out.println("0 - Sair");
            dado = new Scanner(System.in);

            switch (dado.next()){

                case "0": System.exit(0);

                case "1": {
                    break;
                }

                case "2":{
                     grafos.lerListaGrafo();
                } break;

                case "3":{
                    //grafos.menorCaminho(grafo);
                }
            }

        }

    }
}
