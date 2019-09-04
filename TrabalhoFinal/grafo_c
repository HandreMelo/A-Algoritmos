#include <iostream>
#include <conio2.h>
#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<vector<string> > vetorVertices;
vector<string> vetorConexoes;
vector<int> caminhoPassado;

void addCaminho(int i, int j){
	caminhoPassado.push_back(i);
	caminhoPassado.push_back(j);
}
//se for bidirecional, marcar A->B e B->A
void marcar (int i){
	vetorVertices[i][1]="1";
}

void marcar(string a, string b){
	for(int i=0;i<vetorVertices.size();i++){
		if (vetorVertices[i][0] == a || vetorVertices[i][0] == b) {
			for(int j=2;j<vetorVertices[i].size();j+=3){
				if (vetorVertices[i][j] == b || vetorVertices[i][j] == a) {
					vetorVertices[i][j+2]="1";
					return;
					}
				}
			}
		}
}

int converteString(string numS){
	int intS=0;
	stringstream pesoS(numS);
	pesoS >> intS;
	return intS;
}

int pesoTotal=0;
bool achou=false;
bool mudarCaminho=false;

bool busca(string a, string b){
	/*a: b.1;
	>b: a.1-c.2;
	>c: b.2-d.3; <<< da pau*/
	
	bool proximoVertice=false;
	while(!achou){
		int i=0;
		int j=2;
		for(i;i<vetorVertices.size();i++){
			if(vetorVertices[i][0] == a) break;
		}
		for(j;j<vetorVertices[i].size();j+=3){
			if(vetorVertices[i][j] == b) {
				addCaminho(i,j);
				pesoTotal+=converteString(vetorVertices[i][j+1]);
				achou=true;
				cout<<"ACHOU! > ";
				break;
			}
		}
		if(achou)break;
		int cont=0;
		while(cont<vetorVertices.size()){
			bool achouAdjacente=false;
			for(j=2;j<vetorVertices[i].size();j+=3){
				if (vetorVertices[i][j+2]=="0"){
					addCaminho(i,j);
					marcar(vetorVertices[i][0],vetorVertices[i][j]);
					pesoTotal+=converteString(vetorVertices[i][j+1]);
					a=vetorVertices[i][j];
					achouAdjacente=true;
					cout<<a<<"<";
					break;
				}
			}
			if(achouAdjacente) {
			bool achouAdjacente=false;
			break;
			}
			else{
				//marcar(i);
				//pesoTotal-=converteString(vetorVertices[i][j+1]);
				int pos = caminhoPassado[caminhoPassado.size()-4];
				i=pos;
				a = vetorVertices[i][0];
				caminhoPassado.pop_back();
				caminhoPassado.pop_back();
				caminhoPassado.pop_back();
				caminhoPassado.pop_back();
				cont++;
			}
		}
		
	}//while(!achou)
	cout<<"achou?";
}

void mostrar(){
	for(int i=0;i<vetorVertices.size();i++){
		cout<<vetorVertices[i][0];
		cout<<":";
		for(int j=2;j<vetorVertices[i].size();j+=3){
			cout<<vetorVertices[i][j]<<"."<<vetorVertices[i][j+1]<<"F"<<vetorVertices[i][j+2];
			cout<<",";
		}
		cout<<";\n";
	}
}

int main(){
	bool achou = false;
	//int pesoTotal=0;
	string entrada,proximo,peso;
	cout<<"Digitar um vertice por vez. Se no. de conexoes for >1, basta continuar digitando os proximos vertices \n";
	cout<<"digitar ; para o proximo Vertice e ; para finalizar "<<"\n";
	
	do{
		cout<<"Digite um vertice : ";
		//getline(cin,entrada);
		entrada = getche(); cout<<"\n";
		if (entrada==";")break;
		vetorConexoes.push_back(entrada);
		vetorConexoes.push_back("0");	
			
		while (1){
			cout<<"Digite o proximo adjacente ou ok para continuar : ";
			//getline(cin, proximo);
			proximo=getche();
			if (proximo==";") break;
			cout<<"\n";
			cout<<"Digite o peso : ";
			getline(cin, peso);
			vetorConexoes.push_back(proximo);
			vetorConexoes.push_back(peso);
			vetorConexoes.push_back("0");cout<<"\n";
		}
		vetorVertices.push_back(vetorConexoes);
		vetorConexoes.erase(vetorConexoes.begin(),vetorConexoes.end());cout<<"\n";
	}while(1);
	
	mostrar();
	string A,B;
	cout<<"Inicio : ";
	A = getche();cout<<"\n";
	cout<<"Fim : ";
	B = getche();cout<<"\n";
	busca(A,B);
	
	cout<<"Peso Total : "<<pesoTotal<<"\n";
	
	for(int i=0;i<caminhoPassado.size();i+=2){
		int V = caminhoPassado[i];
		int A = caminhoPassado[i+1];
		cout<<"V: "<<vetorVertices[V][0]<<" Adj: "<<vetorVertices[V][A]<<"\n";
	}
	cout<<"?";
	mostrar();
}
