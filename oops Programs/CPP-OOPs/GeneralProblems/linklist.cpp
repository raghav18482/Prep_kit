#include <bits/stdc++.h>
using namespace std;
class Node { 
   public:
   int data; 
   Node *next; 
   Node(int d){
      data = d;
      next =NULL;
   }
}; 

Node* head = NULL; 
Node* temp;

void insert(int new_data) { 
      Node* new_node = new Node(new_data); 
      if(temp==NULL && head==NULL){
         head= new_node;
         temp = new_node;
      }
      else{
         temp->next = new_node;
         temp = new_node;
      }
   } 

void display(Node* root) { 
      Node* ptr;
      ptr = root;
      while (ptr != NULL) { 
         cout<< ptr->data <<" "; 
         ptr = ptr->next; 
      } 
   } 

 Node* rev(Node* root){
      Node* prev=NULL;
      Node* nxt=NULL;
      Node* curr = root;
      while(curr!=NULL){
         nxt = curr->next;
         curr->next = prev;
         prev = curr;
         curr = nxt;
      }
      return prev;
   }

int main() { 
   insert(3);
   insert(1);
   insert(7);
   insert(2);
   insert(9);
   cout<<"The linked list is: ";
   display(head); 
   Node* r;
   cout<<endl;
   r = rev(head);
   display(r);
  return 0; 
}