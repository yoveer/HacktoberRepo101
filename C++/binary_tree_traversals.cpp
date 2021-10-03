#include <bits/stdc++.h>
using namespace std;

class node
{

public:
    int data;
    node *left;
    node *right;

    node()
    {
        data = 0;
        left = NULL;
        right = NULL;
    }
};

void preorder(node *root)
{

    if (root == NULL)
    {
        return;
    }

    cout << root->data << " ";
    preorder(root->left);
    preorder(root->right);
}

void inorder(node *root)
{

    if (root == NULL)
    {
        return;
    }

    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

void postorder(node *root){

if(root==NULL){
    return;
}

postorder(root->left);
postorder(root->right);
cout<<root->data<<" ";

}

int main()
{

    node *root = new node();
    node *left = new node();
    node *right = new node();
    node *left1 = new node();
    node *right1 = new node();
    node *left2 = new node();
    node *right2 = new node();

    root->left = left;
    root->right = right;
    root->left->left = left1;
    root->left->right = right1;
    root->right->left = left2;
    root->right->right = right2;

    root->data = 1;
    left->data = 2;
    right->data = 3;
    left1->data = 4; 
    right1->data = 5;
    left2->data = 6;
    right2->data = 7;

    preorder(root);
    cout << endl;
    inorder(root);
    cout << endl;
    postorder(root);
    return 0;
}