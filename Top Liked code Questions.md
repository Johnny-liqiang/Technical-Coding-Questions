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
- Unlike an array, we don’t need to move all elements past the inserted element. Therefore, you can insert a new node into a linked list in O(1) time complexity.
- It is easy to find out next using the reference field of cur. However, we have to traverse the linked list from the head node to find out prev which will take O(N) time on average, where N is the length of the linked list. So the time complexity of deleting a node will be O(N).
- The space complexity is O(1) because we only need constant space to store our pointers.





