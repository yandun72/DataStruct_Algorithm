class Node:
    def __init__(self,key = None,value=None,pre=None,next=None):
        self.key = key
        self.value = value
        self.pre = pre
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()
        self.length = 0
        #让头节点与尾节点连接
        self.head.next = self.tail
        self.tail.pre = self.head

        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        else:
            node = self.cache[key]
            #然后再把它扔到head后面
            self.move2head(node)
            return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value #已经存在，改变其值，然后扔到链表首位去

            self.move2head(node)
        else:
            node = Node(key = key,value = value)
            #要加入新结点之前，需要判断缓存是否满了
            if self.length == self.capacity:
                #满了需要删除尾部结点,同时也要从cache里面删掉
                self.deletTail()
                self.length -= 1
            #添加在head后面
            self.add2head(node)
            self.cache[key] = node
            self.length += 1
            
    def move2head(self,node):
        #取出前驱和后驱结点
        preNode = node.pre
        postNode = node.next

        #让前驱结点和后驱结点连接起来
        preNode.next = postNode
        postNode.pre = preNode

        #将该结点添加在head后面
        self.add2head(node)


    def deletTail(self):
        #取出尾部结点
        LastNode = self.tail.pre

        #记录它之前的结点
        _ = LastNode.pre

        #让它之前的结点和tail相连
        _.next = self.tail
        self.tail.pre = _

        #删除，释放
        del self.cache[LastNode.key]
        del LastNode

    def add2head(self,node):
        #记录之前的首位结点，让head的next指向node,node的pre指向head,next指向之前的首位结点，之前的首位结点的pre指向node
        rawFirstNode = self.head.next

        self.head.next = node

        node.pre = self.head

        node.next = rawFirstNode

        rawFirstNode.pre = node