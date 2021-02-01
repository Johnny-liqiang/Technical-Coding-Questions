"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        # Creat a Dictionary which holds original nodes as the keys, and the node copies as its values
        #like hashmap
        self.visitedHash ={}  
    
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        # Edge case
        if (head== None):
            return None
        
        # if we already hava a cloned copy of the current node in the visited dictionary, we use the cloned node reference 
        if head in self.visitedHash:
            return self.visitedHash[head]
        
        
        #If we dont have a cloned copy in the visited dictionary
        # create a new node with the value same as old node
        # next and random index as null, and added it into the visited dictionary
        
        node =Node(head.val,None,None)
        
        self.visitedHash[head]=node
        
        #We then make two recursive calls, one using the random pointer and the other using the next pointer. 
        #Essentially, we are making recursive calls for the children of the current node.
        
        node.next=self.copyRandomList(head.next)
        node.random=self.copyRandomList(head.random)
        
        return node
    
    
    
# The basic idea behind the recursive solution is to consider the linked list like a graph. 
# Every node of the Linked List has 2 pointers (edges in a graph). 
# Since, random pointers add the randomness to the structure we might visit the same node again leading to cycles.

#Time cost O(N), where the N is the number of the nodes in the linked list
#Space cost O(N), If we look closely, we have the recursion stack and we also have the space complexity 
#to keep track of nodes already cloned i.e. using the visited dictionary. But asymptotically, the complexity is O(N).
        
        
        
        
        
