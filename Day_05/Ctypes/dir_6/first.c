# include <stdio.h>

int getSum(int* arr, int size){
    int sum =0;

    for(int i=0; i<size; i++){
        sum+=arr[i];
    }
    return sum;
}

int* incArray(int* arr, int size){

    for(int i=0; i<size; i++){
        arr[i]++;
    }
    return arr;
}
