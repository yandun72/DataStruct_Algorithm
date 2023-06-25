from typing import List
import random
class MergeSort:
    def sort(self,data:List):
        self._merge_sort(data,start=0,end=len(data) - 1)

    def swap(self,data,index1,index2):
        data[index1],data[index2] = data[index2],data[index1]

    def merge(self, data: List, start: int, mid: int, end: int):
        """
        合并两个已排序的子列表。

        参数：
            - data: 要合并的列表
            - start: 第一个子列表的起始索引
            - mid: 第一个子列表的结束索引（包含），同时也是第二个子列表的起始索引
            - end: 第二个子列表的结束索引（包含）

        返回：
            无返回值，原地将两个子列表合并为一个已排序的列表
        """

        # 创建一个临时列表来存储合并后的结果
        tmp = []

        # 设置两个指针，分别指向第一个子列表和第二个子列表的起始位置
        index_left = start
        index_right = mid

        # 比较两个子列表的元素，并将较小的元素添加到临时列表中
        while index_left < mid and index_right < end:
            if data[index_left] < data[index_right]:
                tmp.append(data[index_left])
                index_left += 1
            else:
                tmp.append(data[index_right])
                index_right += 1

        # 处理剩余的元素（如果有）并添加到临时列表中
        if index_left < mid:
            tmp.extend(data[index_left:mid])
        elif index_right < end:
            tmp.extend(data[index_right:end])

        # 将临时列表中的元素复制回原始列表中的对应位置
        index = 0
        for i in range(start, end):
            data[i] = tmp[index]
            index += 1


    def _merge_sort(self, data: List, start: int, end: int):
        """
        递归执行归并排序的内部方法，对给定的列表进行排序。

        参数：
            - data: 要排序的列表
            - start: 子列表的起始索引
            - end: 子列表的结束索引（包含）

        返回：
            无返回值，原地对列表进行排序
        """

        # 如果子列表中只有一个元素或者没有元素，不需要进行排序
        if end <= start:
            return

        # 计算子列表的中间索引
        midIndex = start + (end - start) // 2

        # 递归调用_merge_sort()方法，对左半部分子列表进行排序
        self._merge_sort(data, start, midIndex)

        # 递归调用_merge_sort()方法，对右半部分子列表进行排序
        self._merge_sort(data, midIndex + 1, end)

        # 合并两个已排序的子列表
        self.merge(data, start, midIndex, end)




solution = MergeSort()
data = [random.randint(-100,100) for i in range(20)]
print(data)
solution.sort(data)
print(data)
'''
[50, 35, -73, -60, -29, 79, -44, -22, -51, 9, -40, 47, 13, 71, -48, -74, 22, -49, -26, 70]
[-73, -60, -29, -44, -22, -51, 9, -48, -74, -49, -40, -26, 13, 22, 35, 47, 50, 71, 79, 70]
'''