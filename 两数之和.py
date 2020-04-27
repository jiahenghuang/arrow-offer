数组和字符串：

两数之和：给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

代码：

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            number = target - nums[i]
            for j in range(i + 1, len(nums)):
                if nums[j] == number:
                    return [i, j]




def twosum(arr,target):
    n = len(arr)
    for i in range(n):
        num = target - arr[i]
        for j in range(i+1,n):
            if arr[j] == num:
                return [i,j]
                