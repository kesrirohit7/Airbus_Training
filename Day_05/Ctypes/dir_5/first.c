# include <stdio.h>
#include <string.h>
#include <stdlib.h>

void display1(){

    printf("Hare Krishna\n");

}

char* allocMemory(){

    char* data = strdup("Hello World\n");
    printf("Memeory Allocated\n");

    return data;
}


void freeMemory(char* p){

    free(p);

    printf("Memory deallocated\n");

}
