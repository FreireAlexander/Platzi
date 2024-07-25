#include <iostream>

using namespace std;

class Human{

    public: 
        string name;
        int age;

    Human(string _name, int _age=0){
        name = _name;
        age = _age;
    }

};


int main(){

    Human FreirePalomino("Freire Palomino", 20);
    Human SobePalma("Sobe Palma");

    cout << FreirePalomino.name << endl;
    cout << FreirePalomino.age << endl;
    cout << SobePalma.name << endl;
    cout << SobePalma.age << endl;

    return 0;
}