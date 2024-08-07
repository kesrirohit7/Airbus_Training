#include <iostream>
using namespace std;

extern "C"{
    void printMessage(){
        cout<<"Hare Krishna"<<endl;
    }
    void printSum(int a, int b){
        cout<<"Sum of "<<a<<" and "<<b<<" is equal to "<<a+b<<endl; 
    }
}
