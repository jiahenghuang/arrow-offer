#coding:utf-8
'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

#二分查找的概念
class BinFind:
    def Find(self, arr):
        left = 0
        right = len(arr)
        while left < right:
            pos = (left+right) // 2
            if arr[left] < arr[pos]:
                right = pos
            elif arr[left] > arr[pos]:
                left = pos
            else:
                return pos
        return False

if __name__=='__main__':
    Test = BinFind()
    print(Test.Find([3, 4, 5, 1, 2]))
    print(Test.Find([1, 2, 3, 4, 5]))
    print(Test.Find([1, 1, 1, 0, 1]))
    print(Test.Find([1, 0, 1, 1, 1]))
    print(Test.Find([]))
    print(Test.Find([1]))

