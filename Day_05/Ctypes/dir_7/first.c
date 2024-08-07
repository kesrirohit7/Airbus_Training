#include <stdio.h>
#include <stdlib.h> 

struct Point{
    int x;
    int y;
};

void printPoint(struct Point p){
    printf("x : %d, y : %d",p.x,p.y);
    printf("\n");
}

struct Point* getPoint(){
    //struct Point *p;
    struct Point *p = (struct Point *)malloc(sizeof(struct Point));  // Allocate memory for Point
    if (p == NULL) {
        printf("Memory allocation failed\n");
        return NULL;  // Return NULL if memory allocation fails
    }
    p->x=5;
    p->y=2;
    return p;
}
