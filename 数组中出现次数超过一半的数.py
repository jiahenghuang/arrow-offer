#coding:utf-8
'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

#比较水的解法。利用了hash查找时间复杂度为o(1)的特点，用新的空间dict来存储数据。时间复杂度为o(n)

class Solution:
    def find_num(self,array):
        array_count={}
        max = 0
        for i in array:
            if str(i) not in array_count:
                array_count[str(i)]=1
            else:
                array_count[str(i)]+=1
                if array_count[str(i)]>max:
                    max=array_count[str(i)]
                    result = i
        if max > len(array)//2:
            return result
        return 0

if __name__=='__main__':
    arr = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    result = Solution().find_num(arr)
    print(result)