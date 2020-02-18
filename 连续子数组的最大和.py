#coding:utf-8
'''
输入一个整型数组,数组里有整数也有负数。
数组中一二或连续的多个整数组成一个子数组。求所有子数组的和的最大值。
要求时间复杂度为O(n)
'''

#思路：使用递归的思路比较好理解

class Solution:
    # def FindGreatestSumOfSubArray(self, array):
    #     if array == None or len(array) <= 0:
    #         return 0
    #     n_sum = array[0]
    #     largest = n_sum
    #     for i in range(2,len(array)):
    #         if n_sum + array[i] > 0:
    #             n_sum = n_sum +array[i]
    #             if largest < n_sum:
    #                 largest = n_sum
    #         else:
    #             n_sum = array[i]
    #             if n_sum < largest:
    #                 largest = n_sum
    #     return largest
    # 动态规划解决问题
    def FindGreatestSumOfSubArray2(self, array):
        if array == None or len(array) <= 0:
            return 0
        aList = [0]*len(array)
        for i in range(len(array)):
            if i == 0 or aList[i-1] <= 0:
                aList[i] = array[i]
            else:
                aList[i] = aList[i-1] + array[i]
        return max(aList), aList



alist = [1, -2, 3, 10, -4, 7, 2, -5]
s = Solution()
print(s.FindGreatestSumOfSubArray2(alist))





