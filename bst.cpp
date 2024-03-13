#include <iostream>
using namespace std;

// Node structure for the Binary Search Tree
struct node {
    int data;
    node *left;
    node *right;
};

// Binary Tree class
class btree {
public:
    node *root;

    // Constructor to initialize root to NULL
    btree() {
        root = NULL;
    }

    // Function to create nodes in the Binary Search Tree
    node* createnodes(node* root, int data) {
        if (root == NULL) {
            root = new node;
            root->data = data;
            root->left = root->right = NULL;
        } else if (data < root->data) {
            root->left = createnodes(root->left, data);
        } else if (data > root->data) {
            root->right = createnodes(root->right, data);
        }
        return root;
    }

    // Function to insert nodes into the Binary Search Tree
    void insertnodes() {
        int data;
        cout << "Enter the node data: ";
        cin >> data;
        root = createnodes(root, data);
    }

    // Function to display nodes in the Binary Search Tree in inorder
    void inorder_display(node* root) {
        if (root != NULL) {
            inorder_display(root->left);
            cout << root->data << "->";
            inorder_display(root->right);
        }
    }

    // Function to find the minimum value in the Binary Search Tree
    int min_val(node* root) {
        if (root == NULL) {
            return -1;
        }
        while (root->left != NULL) {
            root = root->left;
        }
        return root->data;
    }

    // Function to search for a value in the Binary Search Tree
    void search(int data, node* root) {
        if (root != NULL) {
            if (data == root->data) {
                cout << "Node found" << endl;
            } else if (data < root->data) {
                search(data, root->left);
            } else {
                search(data, root->right);
            }
        } else {
            cout << "Node not found in the bst, try searching another node.." << endl;
        }
    }

    // Function to create the mirror (swap) in the Binary Search Tree
    void mirror(node* root) {
        if (root != NULL) {
            mirror(root->left);
            mirror(root->right);
            node* temp = root->left;
            root->left = root->right;
            root->right = temp;
        }
    }

    // Function to find the length of the longest path in the Binary Search Tree
    int longestpath(node* root) {
        if (root == NULL) {
            return 0;
        }
        int leftCount = longestpath(root->left);
        int rightCount = longestpath(root->right);
        return max(leftCount, rightCount) + 1;
    }
};

// Main function
int main() {
    btree tree;
    int choice, num_nodes = 0;
    int flag = 1;

    // Menu-driven loop
    while (flag == 1) {
        cout << "-------------------------MENU-------------------------" << endl;
        cout << "1. Create the Binary Search tree." << endl;
        cout << "2. Insert nodes in the Binary Search tree." << endl;
        cout << "3. Length of the longest path in the Binary Search tree." << endl;
        cout << "4. Minimum data value in the Binary Search tree." << endl;
        cout << "5. Search a value in the Binary Search tree." << endl;
        cout << "6. Create the mirror (swap) in the Binary Search tree." << endl;
        cout << "Enter your choice from 1-6 : ";
        cin >> choice;

        // Switch-case for menu options
        switch (choice) {
        case 1:
            cout << "Enter the number of nodes in the bst : ";
            cin >> num_nodes;
            for (int i = 0; i < num_nodes; i++) {
                tree.insertnodes();
            }
            tree.inorder_display(tree.root);
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue 0 to exit : ";
            cin >> flag;
            break;
        case 2:
            cout << "Enter the number of nodes to insert in the bst : ";
            cin >> num_nodes;
            for (int i = 0; i < num_nodes; i++) {
                tree.insertnodes();
            }
            tree.inorder_display(tree.root);
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue 0 to exit : ";
            cin >> flag;
            break;
        case 3:
            cout << "Length of the longest path from the root node is : " << tree.longestpath(tree.root) << endl;
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue 0 to exit : ";
            cin >> flag;
            break;
        case 4:
            cout << "The minimum value of the binary is : " << tree.min_val(tree.root) << endl;
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue 0 to exit : ";
            cin >> flag;
            break;
        case 5:
            int data;
            cout << "Enter the node to search in the binary search tree: ";
            cin >> data;
            tree.search(data, tree.root);
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue, 0 to exit: ";
            cin >> flag;
            break;
        case 6:
            tree.mirror(tree.root);
            cout << "Swapped values are : " << endl;
            tree.inorder_display(tree.root);
            cout << "\n------------------------------------------------------" << endl;
            cout << "Enter 1 to continue 0 to exit : ";
            cin >> flag;
            break;
        }
    }
    return 0;
}
