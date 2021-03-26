/*
 * Given two singly linked lists that intersect at some point, find the intersecting
 * node. The lists are non-cyclical.
 *
 * For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the
 * node with value 8.
 * 
 * In this example, assume nodes with the same value are the exact same node objects.
 * 
 * Do this in O(M + N) time (where M and N are the lengths of the lists) and constant
 * space.
 */
#include <iostream>

class Node 
{
public:
    Node(int v)
        : value(v)
        , next(nullptr)
    {}

    Node* GetNext()
    { return next; }
    
    void SetNext(Node *node)
    { if(node != nullptr) next = node; }
    
    int GetValue()
    { return value; }

private:
    Node *next;
    int value;
};

class SinglyLinkedList 
{
public:
    SinglyLinkedList()
        : head(nullptr)
        , tail(nullptr)
    {}
    
    void AddNode(Node *node)
    {
        if(tail == nullptr) {
            head = tail = node;
        } else {
            tail->SetNext(node);
            tail = node;
        }
    }
    
    int GetNodeCount()
    {
        int cnt = 0;
        Node *node = head;
        
        while(node != nullptr) {
            cnt++;
            node = node->GetNext();
        }

        return cnt;
    }
    
    Node* GetHead()
    { return head; }

private:
    Node *head;
    Node *tail;
};


int main(int argc, char **argv)
{
    // build lists
    SinglyLinkedList A, B;
    
    // create nodes - we use stack here
    Node n1(3), n2(7), n3(8), n4(10), n5(99), n6(1);
    A.AddNode(&n1); A.AddNode(&n2); A.AddNode(&n3); A.AddNode(&n4);
    B.AddNode(&n5); B.AddNode(&n6); B.AddNode(&n3); B.AddNode(&n4);
    
    // idea is to get the node count of both lists, traverse the longer list until
    // that node and then compare A to B
    auto l1 = A.GetNodeCount();
    auto l2 = B.GetNodeCount();
    
    Node *a, *b;

    if(l1 > l2) {
        a = A.GetHead();
        b = B.GetHead();
        
        for(int i = 0; i < l1 - l2; ++i)
            if(a->GetNext() != nullptr)
                a = a->GetNext();
    } else {
        a = B.GetHead();
        b = A.GetHead();
        
        for(int i = 0; i < l1 - l2; ++i)
            if(a->GetNext() != nullptr)
                a = a->GetNext();
    }
    
    // compare rest
    while((a != nullptr) && (b != nullptr)) {
        if(a == b) {
            std::cout << a->GetValue() << std::endl;
            break;
        }
        
        a = a->GetNext();
        b = b->GetNext();
    }

    return 0;
}