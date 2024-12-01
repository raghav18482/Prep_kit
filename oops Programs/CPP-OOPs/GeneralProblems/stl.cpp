#include<bits/stdc++.h>

using namespace std;

void main(){
    /*about vector */ 
vector<int> vec; // Empty vector
vector<int> vec(5, 10); // Vector of size 5, initialized with 10s
vector<int> vec = {1, 2, 3, 4, 5}; // Initializer list


vec.insert(vec.begin() + 2, 20); // Inserts 20 at the 3rd position 

vec.clear(); // Removes all elements from the vector

vec = {10, 20, 30, 40, 50};
 // Erase the element at index 2 (which is 30)
 vec.erase(vec.begin() + 2);
 // Output: 10 20 40 50

 // Erase elements from index 1 to 4 (removes 20, 30, and 40)
vec.erase(vec.begin() + 1, vec.begin() + 4);
// Output: 10 50 60

//sorting
sort(vec.begin(), vec.end());

//sort in decending
sort(vec.begin(), vec.end(), greater<int>());

/*about map */ 

map<int, string> ordered_map;               // Ordered map - Stores elements in sorted order (by keys). 
//Insertion, deletion, and search have O(logn) complexity.

unordered_map<int, std::string> unordered_map;   // Unordered map - Stores elements in arbitrary order (no sorting).
//Average time complexity for insertion, deletion, and search is O(1).

ordered_map.insert({1, "one"});
unordered_map.insert({1, "one"});

for (const auto& pair : ordered_map) {
    std::cout << pair.first << ": " << pair.second << std::endl;
}

for (const auto& pair : unordered_map) {
    std::cout << pair.first << ": " << pair.second << std::endl;
}

ordered_map.erase(1);       // Removes the element with key `1`
unordered_map.erase(1);

auto it = ordered_map.find(2);  // Find element with key `2`
if (it != ordered_map.end()) {
    ordered_map.erase(it);      // Remove element if found
}

auto it_u = unordered_map.find(2);
if (it_u != unordered_map.end()) {
    unordered_map.erase(it_u);
}

}