#include <iostream>
#include "includes/material.h"
#include "includes/layers.h"


using namespace std;

int main(){

    cout << "Showing Main File..." << endl;
    Material acier;

    acier.greet();

    cout << endl;

    Layer surface;

    surface.greet();

    return 0;
}