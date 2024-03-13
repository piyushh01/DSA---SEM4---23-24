#include <iostream>
using namespace std;

// Node structure for the tree
struct node {
    char label[10];
    int ch_count;
    struct node *child[10];
} *root;

// General Tree class
class gt {
public:
    int tchapters, i, j, k;

    // Function to create the tree
    void create() {
        root = new node;
        cout << "Enter the name of the book : ";
        cin >> root->label;
        cout << "Enter the number of chapters in the book : ";
        cin >> tchapters;
        root->ch_count = tchapters;

        for (i = 0; i < tchapters; i++) {
            root->child[i] = new node;

            cout << "Enter the chapter " << i + 1 << " name : ";

            cin >> root->child[i]->label;

            cout << "Enter the number of sections in the chapter : ";
            cin >> root->child[i]->ch_count;
            
            for (j = 0; j < root->child[i]->ch_count; j++) {
                
                root->child[i]->child[j] = new node;
                cout << "Enter the section " << j + 1 << " name : ";
                cin >> root->child[i]->child[j]->label;
                cout << "Enter the number of subsections in the section " <<root->child[i]->child[j]->label << " : ";
                cin >> root->child[i]->child[j]->ch_count;
                for (k = 0; k < root->child[i]->child[j]->ch_count; k++) {
                    root->child[i]->child[j]->child[k] = new node;
                    cout << "Enter the subsection " << k + 1 << " name : ";
                    cin >> root->child[i]->child[j]->child[k]->label;
                }
            }
        }
    }

    // Function to display the tree nodes
    void display(node *r1) {
        if (r1 != NULL) {
            cout << "Book title is : " << r1->label << endl;
            for (int i = 0; i < r1->ch_count; i++) {
                cout << "Chapters " << i + 1 << " name : " << r1->child[i]->label << "\n";
                for (int j = 0; j < r1->child[i]->ch_count; j++) {
                    cout << "Section " << j + 1 << " name : " << r1->child[i]->child[j]->label << endl;
                    for (int k = 0; k < r1->child[i]->child[j]->ch_count; k++) {
                        cout << "Sub-section " << k + 1 << " name : " << r1->child[i]->child[j]->child[k]->label << endl;
                    }
                }
            }
        }
    }
};

// Main function
int main() {
    gt obj;
    int flag = 1;
    int choice;
    // Menu-driven loop
    while (flag == 1) {
        cout << "------MENU------" << endl;
        cout << "1. Create" << endl;
        cout << "2. Display" << endl;
        cout << "3. Exit" << endl;
        cout << "Enter your choice from 1-3" << endl;
        cin >> choice;
        // Switch-case for menu options
        switch (choice) {
            case 1:
                obj.create();
                cout << "Enter 1 to continue and 0 to exit : ";
                cin >> flag;
                break;
            case 2:
                obj.display(root);
                cout << "Enter 1 to continue and 0 to exit : ";
                cin >> flag;
                break;
            case 3:
                flag = 0;
                break;
            default:
                cout << "Invalid choice." << endl;
                flag = 0;
                break;
        }
    }
    return 0;
}
