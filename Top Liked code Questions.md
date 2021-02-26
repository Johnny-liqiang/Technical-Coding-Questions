# Linked List
- LC206, 234, 160, 148, 142, 141, 23, 21, 19, 2
- Unlike the array, we are not able to access a random element in a singly-linked list in constant time. 

```
// Definition for singly-linked list.
struct SinglyListNode {
    int val;
    SinglyListNode *next;
    SinglyListNode(int x) : val(x), next(NULL) {}
};
```

- Unlike an array, we don’t need to move all elements past the inserted element. Therefore, you can insert a new node into a linked list in O(1) time complexity





