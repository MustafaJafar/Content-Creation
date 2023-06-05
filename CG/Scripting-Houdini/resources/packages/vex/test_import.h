void test(){
    printf("This is printed from vex external library\n");
}

float get_min_y(int input) {
vector pos = getbbox_min(input); 
return (pos[1]) ;
}
