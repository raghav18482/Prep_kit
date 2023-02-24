#include<bits/stdc++.h>
using namespace std;

int main(){
    int arr[] = {5,4,6,3,7,2,8};
    int n = sizeof(arr)/sizeof(arr[0]);
    sort(arr,arr+n);
    int l=0,r=n;
    int key =9;
    while(l<=r){
        int mid = l +(r-l)/2;
        if(key>arr[mid]){
            l=mid+1;
        }
        else if(key<arr[mid]){
            r = mid-1;
        }
        else{
            cout<<"yes key is present in array";
            break;
        }
    }
    cout<<"key is not present";
}