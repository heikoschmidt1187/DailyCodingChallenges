/*
 * Given a singly linked list and an integer k, remove the kth last element from
 * the list. k is guaranteed to be smaller than the length of the list.
 *
 * The list is very long, so making more than one pass is prohibitively expensive.
 * 
 * Do this in constant space and in one pass.
 */
#include <iostream>

struct Node {
    int val;
    Node *next;
};

Node *head = nullptr;
Node *tail = nullptr;

static void pr();
static void rem(int k);
static void clr();

int main(int argc, char **argv)
{
    // build list
    for(int i = 0; i < 10; ++i) {
        Node *node = new Node();
        node->val = i;
        node->next = nullptr;

        if(head == nullptr)
            head = node;
        else
            tail->next = node;

        tail = node;
    }
    
    // print current list
    pr();

    // remove element
    rem(2);
    
    // print modified list
    pr();
    
    // clear rest of memory
    clr();

    return 0;
}

static void pr()
{
    Node *n = head;

    while(n != nullptr) {
        std::cout << n->val << " ";
        n = n->next;
    }

    std::cout << std::endl;
}

static void rem(int k)
{
    Node *del = nullptr;
    
    if(k == 0) {
        del = head;
        head = head->next;
    } else {
        Node *prev = head;
        del = head->next;

        for(int i = 1; i < k; ++i) {
            prev = del;
            del = del->next;
        }
        
        prev->next = del->next;
    }

    delete del;
}

static void clr()
{
    Node *cur = head;

    while(cur != nullptr) {
        Node *del = cur;
        cur = cur->next;
        delete del;
    }
}