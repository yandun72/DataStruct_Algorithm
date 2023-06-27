from heap import MinHeap

class PriorityQueue(MinHeap):
    def __init__(self,max_size = 128):
        super().__init__()
        self.size = 0
        self.max_size = max_size

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.max_size

    def enqueue(self, item = None, priority = 0):
        if item != None:
            self.insert((priority,item))
        else:
            self.insert(priority)
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        _ = self.pop()
        self.size -= 1

        if isinstance(_,tuple):
            return _[1]
        else:
            return _

if __name__ == '__main__':
    # 示例用法
    pq = PriorityQueue()
    pq.enqueue("Task a", 3)
    pq.enqueue("Task b", 1)
    pq.enqueue("Task c", 2)

    '''
    Processing: Task b
    Processing: Task c
    Processing: Task a
    '''

    while not pq.is_empty():
        task = pq.dequeue()
        print("Processing:", task)
