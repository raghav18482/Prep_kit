#include<bits/stdc++.h>
using namespace std;

class Stack{
    private:
        int stack[1000],top=-1,n=100;
    public:
        void push(int x){
            top++;
            stack[top] = x;
        }
        void pop(){
            top--;
        }
        int Top(){
            return stack[top];
        }
};

int main(){
    Stack s;
    s.push(10);
    s.push(20);
    cout<<s.Top();
    s.pop();
    cout<<s.Top();
    return 0;
}