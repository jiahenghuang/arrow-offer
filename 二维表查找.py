#coding:utf-8

'''
在一个二维数组中，每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

'''
分析：
可以从左上角往右开始查找，查找到arr[0][j]>target时，从第j-1列往下面查找
查找到arr[i][j-1]大于target时，再往右查找，查找到
'''

class Solution:
    # array 二维列表
    def Find(self, array, target):
        if len(array)==0:return 0
        if array is None:return 0
        row ,col = 0,0
        m, n=len(array),len(array[0])
        while row < m and col < n:
            if array[row][col] < target:
                col += 1
            elif array[row][col] > target:
                row += 1
            else:
                return True
        return False

#思考：继续优化，怎样优化，二分查找
class BinFind:
    def Find(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            pos = (left+right) // 2
            if target < arr[pos]:
                right = pos
            elif target > arr[pos]:
                left = pos
            else:
                return pos
        return False

class Solution:   #不想写了，思路就是将某一行某一列剩下到元素做二分查找即可
    def Find(self, array, target):
        if len(array) == 0:return 0
        if array is None:return 0
        row ,col = 0,0
        m, n = len(array),len(array[0])
        while row < m and col < n:
            if array[row][col] < target:
                pass


if __name__=='__main__':
    arr=[1,3,6,9,40,50]
    print(BinFind().Find(arr,9))

    # array = [[1, 2, 8, 9],
    #      [2, 4, 9, 12],
    #      [4, 7, 10, 13],
    #      [6, 8, 11, 15]]
    # print(Solution().Find(array,90))
