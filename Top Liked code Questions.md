# Linked List
- LC206, 234, 160, 148, 142, 141, 23, 21, 19, 2
- Unlike the array, we are not able to access a random element in a singly-linked list in constant time. 

```
C++:
// Definition for singly-linked list.
struct SinglyListNode {
    int val;
    SinglyListNode *next;
    SinglyListNode(int x) : val(x), next(NULL) {}
};
Python:
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  # sentinel node as pseudo-head
```
- Unlike an array, we don’t need to move all elements past the inserted element. Therefore, you can insert a new node into a linked list in O(1) time complexity.
- It is easy to find out next using the reference field of cur. However, we have to traverse the linked list from the head node to find out prev which will take O(N) time on average, where N is the length of the linked list. So the time complexity of deleting a node will be O(N).
- The space complexity is O(1) because we only need constant space to store our pointers.
- Two pointers starts at different position: one starts at the beginning while another starts at the end;
- Two pointers are moved at different speed: one is faster while another one might be slower.
- For a singly linked list, since we can only traverse the linked list in one direction, the first scenario might not work. 
- LC707
```
class Listnode:
    def __init__(self,x):
        self.val=x
        self.next=None
        '''
        define the linklist the node content: the reference/point  and the value
        '''    
    
        
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size =0             #initial the list size equal to 0 and the first node as the head
        self.head = Listnode(0) # sentinel node as pseudo-head

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index <0 or index>=self.size: # started at 0 indexed
            return -1
        
        currnode=self.head
        
        for i in range(index+1): # need to visit from the sentinel node/ head to the current node, need O(N) Time Complexity 
            currnode=currnode.next  #  check the listnode we executor index times so we get the index-th currentnode
            
        return currnode.val

    
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        
        self.addAtIndex(0,val)
        
        

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val) # list from 0 to size-1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        # If index is greater than the length, the node will not be inserted
        if index> self.size:
            return 
        # if the index small than 0, force it into 0 and added at the beginning 
        if index<0:
            index=0
            
               
        new_node=Listnode(val)
        
        current=self.head
        for i in range(index): # get the current node of the index-1 :check the get method 
            current=current.next
                                            
        new_node.next=current.next # link new node to the current index-1 node.next = old indexth node
        current.next=new_node # be careful the order
        
        self.size +=1
        
        
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index>= self.size or index <0:
            return 
        
        current=self.head
        for i in range(index): # get the current node of the index-th :check the get method 
            current=current.next
        
        current.next=current.next.next
        self.size -=1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


```





