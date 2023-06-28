'''
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

输入: nums = [1], k = 1
输出: [1]
'''
from heap import MaxHeap
from collections import Counter,defaultdict
import random
random.seed(42)
K = 2
data = [1,1,1,2,2,3]

def func():
    myheap = MaxHeap() #最大堆

    counts = Counter(data)
    counts2 = defaultdict(list)
    for key,value in counts.items():
        counts2[value].append(key) 
    
    for key,value in counts2.items():
        myheap.insert((key,tuple(value)))

    print(myheap.heap)

    res = []
    for i in range(len(counts2)):
        _ = myheap.pop()
        print(i,_)
        res.extend(list(_[1]))
        if len(res) >= K:
            break
        
    return res[0:K]

print('res = ',func())