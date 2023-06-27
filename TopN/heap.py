class Heap:
    def __init__(self):
        self.heap = []
    
    def parent(self,index):
        
        return (index - 1) // 2

    def left_child(self,index):

        return 2 * index + 1

    def right_child(self,index):

        return 2 * index + 2
    
    def __len__(self):

        return len(self.heap)
    
    def swap(self,i,j):

        self.heap[i],self.heap[j] = self.heap[j],self.heap[i] 
    
    def insert(self,value):

        self.heap.append(value)

        self._sift_up(len(self.heap) - 1)
    
    def getTopElem(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]

    def pop(self):
        
        pass
        

    #插入元素后，就需要从底向上维护堆的性质
    def _sift_up(self,i):
    
        pass
    
    #删除根元素后，就需要从顶到底维护堆的性质
    def _sift_down(self,i):

        pass


class MaxHeap(Heap):
    def __init__(self):
        super().__init__()
    
    def _sift_up(self, i):
        
        while i > 0 and self.heap[self.parent(i)] < self.heap[i]:
            self.swap(self.parent(i),i)
            i = self.parent(i)
    
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        max_val = self.getTopElem()
        self.swap(0,len(self.heap) - 1) #先将根部和最后一个元素互换位置
        self.heap.pop() #根部移动到最后位置去了，就可以pop掉
        self._sift_down(0) #自顶向下重新维护一下堆
        return max_val


    def _sift_down(self,i):

        max_index = i #假定最大值的索引为根节点

        left_child_index = self.left_child(i)

        right_child_index = self.right_child(i)

        
        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[max_index]:
            max_index = left_child_index
        
        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[max_index]:
            max_index = right_child_index
        
        if max_index != i: #发现最大值并非根节点，就需要调整
            self.swap(i,max_index)
            self._sift_down(max_index) #继续递归下去
        


class MinHeap(Heap):
    def __init__(self):
        super().__init__()
    
    def _sift_up(self, i):
        
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i,self.parent(i))
            i = self.parent(i)
    
    def pop(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        
        min_val = self.getTopElem()

        self.swap(0,len(self.heap) - 1)

        self.heap.pop()
        
        self._sift_down(0)

        return min_val


    def _sift_down(self,i):
        
        min_index = i

        left_child_index = self.left_child(i)

        right_child_index = self.right_child(i)

        if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[min_index]:
            min_index = left_child_index
        
        if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[min_index]:
            min_index = right_child_index
    
        if min_index != i:
            self.swap(min_index,i)
            self._sift_down(min_index)

if __name__ == '__main__':

    '''
    最大堆
    [(8, 'orange'), (5, 'apple'), (3, 'banana'), (2, 'grape')]
    最小堆
    [(2, 'grape'), (3, 'banana'), (5, 'apple'), (8, 'orange')]
    '''

    for _ in [MaxHeap,MinHeap]:
        heap = _()

        heap.insert((5, 'apple'))
        heap.insert((3, 'banana'))
        heap.insert((8, 'orange'))
        heap.insert((2, 'grape'))
        tmp = []
        for i in range(len(heap)):
            tmp.append(heap.pop())  
        print(tmp)
        
    
