#include <iostream>
#include <fstream>

using namespace std;

int main(){

    string name = "freire";
    int number = 123456;

    string StrNumber = to_string(number);

    for(int i=0; i <= 5;i++){
        cout << "Inicial: " << name[i] << endl;
        cout << "Number: " << StrNumber[i] << endl;
    }

    cout << "Lenght of name: " << name.length();

    bool isHappy = true;
    int integer;
    do{
        cout << "\n Ingrese el valor: ";
        cin >> integer;
        cout << endl;
        if(integer < 100){
            isHappy = false;
        }
    }while(isHappy);

    return 0;
}