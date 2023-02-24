#include<bits/stdc++.h>
using namespace std;

class Node{
    public:
    int data;
    Node *next;
    Node *prev;
};

Node *tail= NULL;
Node *head = NULL;
void insert(int data){
    Node *newnode = new Node();
    newnode->data = data;
    newnode->prev = tail;
    newnode->next = NULL;
    if(tail == NULL){
        head = newnode;
    }
    if(newnode->prev != NULL){
        tail->next = newnode;
    }
    tail = newnode;
}


void display() { 
   Node* ptr;
   ptr = head;
   while (ptr != NULL) { 
      cout<< ptr->data <<" "; 
      ptr = ptr->next; 
   } 
} 

void reverse(){
    Node* temp;
    temp =tail;
    while(tail!=NULL){
        cout<<temp->data<<" ";
        temp=temp->prev;
    }
}

int main() { 
   Node n;
   insert(3);
   insert(1);
   insert(7);
   insert(2);
   insert(9);
   cout<<"The linked list is: ";
   display(); 
   cout<<"Reverse of linked list is: ";
   reverse();
  return 0; 
}