/*Test Import Library. 

This library was made to test importing custom scripts.
you can test in houdini as follows: 
1. create "Add" node, and click "+" button
2. create "point wrangle" node and add this code:


#include "test_import.h"
test();

*/


void test(){
    printf("This is printed from vex external library\n");
}

float get_min_y(int input) {
vector pos = getbbox_min(input); 
return (pos[1]) ;
}
