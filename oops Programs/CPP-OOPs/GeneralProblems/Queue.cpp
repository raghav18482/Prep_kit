#include<bits/stdc++.h>
using namespace std;
class Queue{
    private:
        int q[1000],n=1000,f=-1,r=-1;
    public:
        void push(int x){
            if(f==-1){
                f=0;
            }
            r++;
            q[r]=x;
        }
        void pop(){
            f++;
        }
        int front(){
            return q[f];
        }
};

int main(){
    Queue qu;
    qu.push(10);
    qu.push(12);
    qu.pop();
    cout<<qu.front();
}