# Hashmap + DoubleLinkedList
# The problem can be solved with a hashmap that keeps track of the keys and its values in the double linked list. 
# That results in \mathcal{O}(1)O(1) time for put and get operations and allows to remove the first added node in \mathcal{O}(1)O(1) time as well.
# One advantage of double linked list is that the node can remove itself without other reference. 
# In addition, it takes constant time to add and remove nodes from the head or tail.
# One particularity about the double linked list implemented here is that there are pseudo head and pseudo tail to mark the boundary,
# so that we don't need to check the null node during the update.

from typing import List
def lruCacheMisses(num: int, pages : List[int], maxCacheSize : int) -> int:
    class DLL: #  DoubleLinkedList
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.next = None
            self.prev = None
    
    class LRUCache:      
        def __init__(self, capacity: int):
            self.m = {}
            self.head = DLL(0,0)
            self.tail = DLL(0,0)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
            self.capacity = capacity
            
        def get(self, key: int) -> int:
            """
            :type key: int
            :rtype: int
            """
            if key in self.m:
                loc = self.m[key]
                loc.prev.next = loc.next
                loc.next.prev = loc.prev
                self.head.next.prev = loc
                loc.next = self.head.next
                self.head.next = loc
                loc.prev = self.head
                return loc.val
            else:
                return -1
        def put(self, key: int, value: int) -> None:
            
            """
            :type key: int
            :type value: int
            :rtype: void
            """
            if key in self.m:
                self.get(key)
                self.m[key].val = value
                return
            self.size += 1
            
            if self.size > self.capacity:
                lru = self.tail.prev
                del self.m[lru.key]
                self.tail.prev.val = self.tail.val
                self.tail.prev.next = None
                self.tail = self.tail.prev
                self.size -= 1
            new_head = DLL(key, value)
            self.head.next.prev = new_head
            new_head.next = self.head.next
            self.head.next = new_head
            new_head.prev = self.head
            self.m[key] = new_head
    cache = LRUCache(maxCacheSize)
    misses = 0
    for page in pages:
        if cache.get(page) == -1:
            misses += 1
        cache.put(page, None)
    return misses
    
    
#Time complexity : O(1) both for put and get.
#Space complexity : )O(capacity) since the space is used only for a hashmap and double linked list with at most capacity + 1 elements.
