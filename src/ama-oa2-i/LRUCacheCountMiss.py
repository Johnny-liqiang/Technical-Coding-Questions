from typing import List
def lruCacheMisses(num: int, pages : List[int], maxCacheSize : int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    class LRUCache:
        class DLL:
            def __init__(self, key, val):
                self.key = key
                self.val = val
                self.next = None
                self.prev = None
        def __init__(self, capacity: int):
            self.m = {}
            self.head = self.DLL(0,0)
            self.tail = self.DLL(0,0)
            self.head.next = self.tail
            self.tail.prev = self.head
            self.size = 0
            self.capacity = capacity
        def get(self, key: int) -> int:
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
            new_head = self.DLL(key, value)
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
