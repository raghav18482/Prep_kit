#include<bits/stdc++.h>
using namespace std;
int main(){
    int num=4; //-> 0100
    int arr[32] = {0};
    int i=31;
    while(num>=0){
        if(num%2!=0){
            arr[i]=1;
        }
        i--;
        num = num/2;
    }
    for(int j=0;j<33;j++){
        cout<<arr[j]<<" ";
    }
}