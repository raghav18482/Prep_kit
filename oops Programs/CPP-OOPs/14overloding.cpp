//it is a compile time polymorphism
//overloading is a static binding and overidding is dynamic binding
#include<bits/stdc++.h>
using namespace std;
class Area{
    public:
        void area(int x){
            cout<<x*x<<endl;
        }
        void area(int a,int b){
            cout<<a*b;        }
};
int main(){
    Area square;
    Area rectangle;
    square.area(4);
    rectangle.area(2,3);
    return 0;s
}
//The return type of a function has no effect on function overloading, therefore the same function signature with different return type will not be overloaded. 