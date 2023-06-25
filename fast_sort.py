from typing import List
import random
class FastSort:
    def sort(self,data:List):
        self._quick_sort(data,start=0,end=len(data) - 1)
    
    def _partion(self,data,start,end):
        randomIndex = random.randint(start,end)
        self.swap(data,start,randomIndex)
        pivot = data[start]

        le,ge = start + 1,end
        while True:
            while data[ge] > pivot and ge >= le:
                ge -= 1
            while data[le] < pivot and ge >= le:
                le += 1
            if le >= ge:
                break
            self.swap(data,le,ge)
            ge -= 1
            le += 1
        self.swap(data,ge,start) #把最开始的位置扔到中间去
        return ge

    def swap(self,data,index1,index2):
        data[index1],data[index2] = data[index2],data[index1]

    def _quick_sort(self,data:List,start:int,end:int):
        if end <= start:
            return      
        pivotIndex = self._partion(data,start,end)
        self._quick_sort(data,start,pivotIndex)
        self._quick_sort(data,pivotIndex+1,end)

solution = FastSort()
data = [random.randint(-100,100) for i in range(20)]
print(data)
solution.sort(data)
print(data)
'''
[-93, -3, -42, 86, 26, 98, 98, -78, -74, -88, 78, -31, 61, -14, -90, -1, -98, 5, 86, -72]
[-98, -93, -90, -88, -78, -74, -72, -42, -31, -14, -3, -1, 5, 26, 61, 78, 86, 86, 98, 98]
'''