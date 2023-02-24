#include<bits/stdc++.h>
using namespace std;

int main(){
    vector<int> arr;
    cout<<"enter value in array";
    for(int i=0;i<6;i++){
        int x;
        cin>>x;
        arr.push_back(x);
    }
    int n = arr.size();
    sort(arr.begin(),arr.end()-n/2);
    sort(arr.begin()+n/2,arr.end(),greater<int>());
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
}