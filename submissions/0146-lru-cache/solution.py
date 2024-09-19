class ListNode:
    def __init__(self, val, key=None, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    """

    LRU w <-> y <-> z <-> x MRU    

    HashMap : {w: node_w, x: node_x, y, z}
            
    """

    def __init__(self, capacity: int):
        #1. hashmap with size capacity
        #2. initialize the LL

        self.capacity = capacity
        self.hashmap = {}
        self.LRU = ListNode(None)
        self.MRU = ListNode(None, None, None, self.LRU)
        self.LRU.next = self.MRU

    # def print_LRU(self):
    #     node = self.LRU
    #     while node != self.MRU:
    #         node = node.next
    #         print(node.val, end=' ')

    #     print("")

    # def print_MRU(self):
    #     node = self.MRU
    #     while node != self.LRU:
    #         node = node.prev
    #         print(node.val, end=' ')

    #     print("")

    def get(self, key: int) -> int:
        # 1. Look up hashmap and retrieve val
        if key in self.hashmap:
            val = self.hashmap[key].val
            
            #2. move val to MRU     
            #       ... <-> a <-> z <-> ... <-> x <- MRU
            self.hashmap[key].prev.next = self.hashmap[key].next
            self.hashmap[key].next.prev = self.hashmap[key].prev

            self.hashmap[key].prev = self.MRU.prev
            self.hashmap[key].next = self.MRU
            self.MRU.prev.next = self.hashmap[key]
            self.MRU.prev = self.hashmap[key]
            
            # self.print_LRU()
            # self.print_MRU()
            return val
        else: 
            # self.print_LRU()
            # self.print_MRU()

            return -1

    def put(self, key: int, value: int) -> None:
       
        if key in self.hashmap:  # case 1: key exists
    
            # update node value
            self.hashmap[key].val = value

            # move to MRU        
            self.hashmap[key].prev.next = self.hashmap[key].next
            self.hashmap[key].next.prev = self.hashmap[key].prev

            self.hashmap[key].prev = self.MRU.prev
            self.hashmap[key].next = self.MRU
            self.MRU.prev.next = self.hashmap[key]
            self.MRU.prev = self.hashmap[key] 

        else:   # case 2: new key

            # remove LRU if max capacity
            if len(self.hashmap) == self.capacity:  
                # Remove LRU if full
                    #1. get the node to be removed
                    to_remove = self.LRU.next

                    #2. update LRU ptr to new LRU
                    self.LRU.next = to_remove.next

                    #2.5 update new LRU to point to LRU
                    to_remove.next.prev = self.LRU
                    
                    
                    #3. remove the node from self.hashmap
                    self.hashmap.pop(to_remove.key, None)

            # create node for new key
            new_node = ListNode(value, key, next=self.MRU, prev=self.MRU.prev)

            # insert into self.hashmap and LL at MRU 
            self.MRU.prev.next = new_node
            self.MRU.prev = new_node

            self.hashmap[key] = new_node
    
        # self.print_LRU()
        # self.print_MRU()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
