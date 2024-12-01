#include <bits/stdc++.h>

using namespace std;

int main() {
    string str1; // Empty string
    string str2("Hello, World!"); // Initialize with a C-string
    string str3 = "C++ Programming"; // Copy initialization
    string str4(str2); // Copy constructor
    string str5(5, 'A'); // Initializes with 5 'A' characters
    str3.append(" Language"); //C++ Programming Language

    //adding int to string without to_string() opertion
    int i=3;
    string s;
    s.push_back(i+'0');//(i+'0') means 48+3
    cout<<s<<endl;//3
    s.clear();
    s.push_back(48+i);//48 is the aasci value of 0
    cout<<s<<endl;//3

    cout << str1 << "\n" << str2 << "\n" << str3 << "\n" << str4 << "\n" << str5<<"\n"<<str3 << endl;
    str3.insert(4, "Heigh Level "); //C++ Heigh LevelProgramming Language
    cout<<str3<<endl;
    str3.erase(4, 12);//(index,count) C++ Programming Language
    cout<<str3<<endl;
    cout<<str3.find("Lang")<<endl;//16
    cout<<str3.find_first_of("+")<<endl;//1
    reverse(str2.begin(), str2.end());
    cout<<str2<<endl;
    str2.erase(remove(str2.begin(), str2.end(), ','), str2.end()); // Removes all commas
    cout << str2<<endl;
    cout<<str3.substr(0,3)<<endl;//c++
    char c = str3.back();//take last character
    str3.pop_back();//remove from last
    str3 = c + str3; 
    cout<<str3<<endl;//str3.pop_back()

    
    return 0;
}
