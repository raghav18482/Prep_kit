// Binary Search Tree operations in C++
#include <iostream>
using namespace std;

class node {
 public:
  int key;
  node *left, *right;
  node(int item){
    key = item;
    left = right = NULL;
  }
};

// Inorder Traversal
void inorder(node *root) {
  if (root != NULL) {
    // Traverse left
    inorder(root->left);
    // Traverse root
    cout << root->key << " -> ";
    // Traverse right
    inorder(root->right);
  }
}

// Insert a node
node *insert(node *Node, int key) {
  // Return a new node if the tree is empty
  if (Node == NULL) {
    node *newnode = new node(key);
    return newnode;
  }
  // Traverse to the right place and insert the node
  if (key < Node->key)
    Node->left = insert(Node->left, key);
  else
    Node->right = insert(Node->right, key);

  return Node;
}

int findminfromright(node* root){
        while(root->left!=nullptr)
            root=root->left;
        return root->key;
}

node* deleteNode(node* root, int val) {
    if(root==nullptr) return root;
    else if(root->key>val) root->left=deleteNode(root->left,val);
    else if(root->key<val) root->right=deleteNode(root->right,val);
    else{//if left , right or both childs are NULL
        if(root->right==nullptr){
            return root->left;
        }
        else if(root->left==nullptr){
          return root->right;
        }
        else{
		    //replace the root value by find the minimum val from right side 
            root->key=findminfromright(root->right);
            root->right = deleteNode(root->right, root->key);
        }
    }
    return root;
}

// Driver code
int main() {
  node *root = NULL;
  root = insert(root, 8);
  root = insert(root, 3);
  root = insert(root, 1);
  root = insert(root, 6);
  root = insert(root, 7);
  root = insert(root, 10);
  root = insert(root, 14);
  root = insert(root, 4);

  cout << "Inorder traversal: ";
  inorder(root);

  cout << "\nAfter deleting 10\n";
  root = deleteNode(root, 10);
  cout << "Inorder traversal: ";
  inorder(root);
}