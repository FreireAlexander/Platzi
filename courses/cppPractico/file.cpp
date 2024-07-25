#include <iostream>
#include <fstream>

using namespace std;

int main(){

    ofstream MyFile("Saved.txt");

    if(MyFile.is_open()){
        MyFile << "Hola Freire\n";
        MyFile << "Otra Linea\n";
    }

    MyFile.close();

    ifstream ReadFile("Saved2.txt");
    string line;
    int i = 0;
    if(ReadFile.is_open()){
        while(getline(ReadFile, line)){
            cout << "Leyendo linea{" << i << "} " << line << endl;
            i+=1;
        }
    }
    
    ReadFile.close();

    return 0;
}