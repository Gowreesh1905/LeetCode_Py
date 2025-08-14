class Node:
    def __init__(self,key,value):
        self.key=key
        self.val=value
        self.prev=None
        self.next=None

    def delete(self):
        l=self.prev
        r=self.next
        l.next=r
        r.prev=l
        self.next=None
        self.prev=None

    def insert(self,head):
        r=head.next
        head.next=self
        self.prev=head
        r.prev=self
        self.next=r





class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.count=0
        self.map={}
        self.head=Node(-1,-1)
        self.tail=Node(-1,-1)
        self.head.next=self.tail
        self.tail.prev=self.head


        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if not (key in self.map):
            return -1

        res=self.map[key]
        res.delete()
        res.insert(self.head)
        return res.val


        
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key not in self.map:

            if self.capacity==self.count:
                temp=self.tail.prev
                k=temp.key
                temp.delete()
                del self.map[k]
                self.count-=1
                
            node=Node(key,value)
            node.insert(self.head)

            self.map[key]=node
            self.count+=1

        else:
            node=self.map[key]
            node.val=value
            node.delete()
            node.insert(self.head)
        
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)