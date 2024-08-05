#include <stdio.h>


enum weekDays {Sunday, Monday, Tuesday, Wendnesday, Thursday, Friday, Saturday};

int main(){
    enum weekDays today;
    today = Monday;
    printf("Day %d", today+1);
    
    return 0;
}