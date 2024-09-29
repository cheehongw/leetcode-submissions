class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.set = set()
        self.next = next
        self.prev = prev


class AllOne:

    def __init__(self):
        self.map = {}
        self.min = ListNode(None, None, None)
        self.max = ListNode(None, self.min, None)
        self.min.next = self.max
    
    def _insert(self, val, node_before):
        newNode = ListNode(val, node_before, node_before.next)
        node_before.next.prev = newNode
        node_before.next = newNode
        return newNode

    def _remove(self, node_to_remove):
        node_to_remove.prev.next = node_to_remove.next
        node_to_remove.next.prev = node_to_remove.prev

    def inc(self, key: str) -> None:
        if key not in self.map:
            # key is new, insert into ListNode = 1
            
            # ListNode == 1 does not exist, create Node first
            if self.min.next.val != 1:
                newNode = self._insert(1, self.min)
            
            #ListNode == 1 now exists, add key into ListNode and point key entry to listnode
            self.min.next.set.add(key)
            self.map[key] = self.min.next
        else:
            #key exists, promote to next ListNode

            curr_node = self.map[key]
            expected_next_val = curr_node.val + 1
            next_node = curr_node.next

            #next ListNode does not exist, create node first
            if (next_node.val != expected_next_val):
                next_node = self._insert(expected_next_val, curr_node)
            
            # next listnode exists, add key to ListNode and point key entry to new listnode
            next_node.set.add(key)
            self.map[key] = next_node

            # remove key from prev ListNode and remove prevListNode if it is empty
            curr_node.set.remove(key)
            if len(curr_node.set) == 0:
                self._remove(curr_node)

    def dec(self, key: str) -> None:
        curr_node = self.map[key]
        count = curr_node.val

        if count == 1:
            # remove the key from ListNode
            curr_node.set.remove(key)

            # remove ListNode(1) if it is empty
            if len(curr_node.set) == 0:
                self._remove(curr_node)

            # delete entry from map
            self.map.pop(key)
        
        else:
            new_count = count - 1
            prev_node = curr_node.prev

            if prev_node.val != new_count:
                # prev ListNode does not exist, create node first
                prev_node = self._insert(new_count, prev_node)

            # prev node exists, add key to ListNode and point key entry to new listnode
            prev_node.set.add(key)
            self.map[key] = prev_node

            curr_node.set.remove(key)
            if len(curr_node.set) == 0:
                self._remove(curr_node)

    def getMaxKey(self) -> str:
        if self.max.prev == self.min:
            return ""
        else:
            elem = self.max.prev.set.pop()
            self.max.prev.set.add(elem)
            return elem

    def getMinKey(self) -> str:
        if self.min.next == self.max:
            return ""
        else:
            elem = self.min.next.set.pop()
            self.min.next.set.add(elem)
            return elem


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
