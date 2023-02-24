#include<bits/stdc++.h>
using namespace std;

class LRUCache {
public:
    int n=0;
    list<int> v;
    unordered_map<int,int> mp;//(page , value)
    LRUCache(int capacity) {
        n= capacity;
    }
    
    int get(int key) {
        if(mp.find(key)!=mp.end()){//found in map
            v.remove(key);// remove from list and make it most recntly use by push_back 
            v.push_back(key);
            return mp[key];
        }
        else{
            return -1;
        }
    }
    
    void put(int key, int value) {
        if(mp.find(key)==mp.end()){
            if(v.size()==n){//if cache is full and not in map
                int k = v.front();
                v.pop_front();
                mp.erase(k);
            }
        }
        else{//if present in cache not update the chache
            v.remove(key);//o(n) time complexity
        }
        mp[key] = value;
        v.push_back(key);
    }
};


int main(){
    LRUCache l1(2);
    int i=0;
    l1.put(1,1);
    l1.put(2,2);
    cout<<l1.get(1)<<" ,";//which page is present in process no.1
    l1.put(3,3);
    cout<<l1.get(2);//which page is present in process no.2
    return -1;
}

//but this is o(n)
// try below code

/* class LRU{
public:
 
    struct Node{
        int key;
        int value;
        Node* prev;
        Node* next;
    };
 
    Node* head;
    Node* tail;
    int size, cap;
    unordered_map<int, Node*> mp;
 
    Node* createNode(int k, int v){
        Node* x = new Node();
        x->key = k;
        x->value = v;
        x->next = head->next;
        head->next = x;
        x->prev = head;
        x->next->prev = x;
 
        mp[k] = x;
 
        return x;
    }
 
    void moveToHead(Node* x){
        if(head->next == x){
            return;
        }
 
        x->prev->next = x->next;
        x->next->prev = x->prev;
 
        x->next = head->next;
        head->next->prev = x;
        //x->next->prev = x;
        head->next = x;
        x->prev = head;
 
    }
 
 
    void removeTail(){
        Node* x = tail->prev;
        x->prev->next = tail;
        tail->prev = x->prev;
 
        mp.erase(x->key);
    }
 
    LRUC(int capacity) {
        head = new Node();
        tail = new Node();
        head->next = tail;
        tail->prev = head;
        size = 0;
        cap = capacity;
    }
 
    void printList(){
        Node* tmp = head->next;
        while(tmp!= tail){
            cout<<tmp->key<<" ";
            tmp = tmp->next;
        }
        cout<<endl;
    }
 
    int get(int k) {
        //cout<<"inGet"<<endl;
        if(mp.find(k) == mp.end()){
            return -1;
        }
        Node* x = mp[k];
        moveToHead(x);
 
        //printList();
 
        return x->value;
    }
 
    void put(int k, int v) {
        //cout<<"inPut"<<endl;
 
        if(mp.find(k) != mp.end()){
            //key already present
            Node* x = mp[k];
            x->value = v;
            moveToHead(x);
            return;
        }
 
        createNode(k,v);
        if(size < cap){
            size++;
            //printList();
            return ;
        }
        else{
            removeTail();
            //printList();
        }
    }
};/*