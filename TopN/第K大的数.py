import random
random.seed(42)
from PriorityQueue import PriorityQueue
import time

def time_count(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(f'耗费时间:{round((end - start)*1000,2)}ms')
        return res
    return wrapper

data =[ random.randint(-1000,1000) for i in range(10000) ]

K = 1000

class Solution_1:
    @time_count
    def findKlargestNum(self,data,K):
        queue = PriorityQueue()
        for d in data:
            queue.enqueue(priority=d)
        
        for i in range(len(data) - K + 1):
            res = queue.dequeue()
        return res
    

class Solution_2:
    @time_count
    def findKlargestNum(self,data,K):
        self.K = K

        self.targetIndex = len(data) - K

        self.quick_sort(data,0,len(data) - 1)

        return data[self.targetIndex]
    
    def swap(self,data,i,j):
        data[i],data[j] = data[j],data[i]

    def partion(self,data,start,end):
        randomIndex = random.randint(start,end)
        self.swap(data,randomIndex,start)

        left = start
        le = start + 1
        ge = end

        while True:
            while le <= ge and data[ge] > data[left]:
                ge -= 1
            
            while le <= ge and data[le] < data[left]:
                le += 1
            
            if le >= ge:
                break

            self.swap(data,le,ge)
            le += 1
            ge -= 1
        
        self.swap(data,left,ge)
        return ge

    def quick_sort(self,data,start,end):
        if start >= end:
            return
        pivotIndex = self.partion(data,start,end)

        if pivotIndex == self.targetIndex:
            return

        elif pivotIndex > self.targetIndex:#往左边找
            self.quick_sort(data,start,pivotIndex)
        
        else:
            self.quick_sort(data,pivotIndex + 1,end)
        

class Solution_3:
    @time_count
    def findKlargestNum(self,data,K):
        self.K = K

        data.sort()

        
        return data[len(data) - K]


s1 = Solution_1()
print(s1.findKlargestNum(data,10))     
    
s2 = Solution_2()
print(s2.findKlargestNum(data,10))

s3 = Solution_3()
print(s3.findKlargestNum(data,10))

'''
耗费时间:69.81ms
997
耗费时间:3.02ms
997
耗费时间:0.97ms
997
'''
