#coding:utf-8
#求数据流中的中位数

# 思路：用大顶堆加小顶堆，因为堆的调整的时间复杂度是o(logn)
# 排序的方式是：大顶堆的堆顶的元素要小于小顶堆的堆顶的。这样可以保证大顶堆的所有元素都是小于小顶堆的。
# 将一个元素放在大顶堆堆顶，然后堆这个大顶堆进行调整，加入大顶堆有k个元素，这个调整堆的时间复杂度是o(logk)
# 有一个小顶堆的概念。

from heapq import *
class Solution:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    def Insert(self, num):
        if (len(self.min_heap)+len(self.max_heap))&1:
            if len(self.min_heap)>0 and num>self.min_heap[0]:
                heappush(self.min_heap, num)
                heappush(self.max_heap, -self.min_heap[0])
                heappop(self.min_heap)               
            else:
                heappush(self.max_heap, -num)
            
        else:
            if len(self.max_heap)>0 and num<-self.max_heap[0]:
                heappush(self.max_heap, -num)
                heappush(self.min_heap, -self.max_heap[0])
                heappop(self.max_heap)
            else:
                heappush(self.min_heap, num)
    def GetMedian(self, n=None):
        # write code here
        if (len(self.min_heap)+len(self.max_heap))&1:
            mid = self.min_heap[0]
        else:
            mid = (self.min_heap[0]-self.max_heap[0])/2.0
        return mid
 


