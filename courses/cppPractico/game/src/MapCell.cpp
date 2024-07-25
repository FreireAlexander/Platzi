#include <iostream>

#include "../headers/MapCell.h"

using namespace std;

MapCell::MapCell(int _id){
    id = _id;
}

void MapCell::greet(){
    cout << "Hello I am a cell" << endl;
    cout << "Printing id: " << id << endl;
}


