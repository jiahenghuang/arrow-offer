#coding:utf-8
'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

#思路：双指针
#divP指向左边最后一个奇数，searchP指向右边第一个奇数

class Solution():
    def reOrderArray(self, array):
        divP = 0
        for i in range(len(array)):
            if array[i]%2 == 1:
                searchP = i
                while searchP > divP:
                    array[searchP],array[searchP-1] = array[searchP-1],array[searchP]
                    searchP -= 1
                divP += 1
        return array

if __name__=='__main__':
    array=[1,2,3,6,9,4]
    print(Solution().reOrderArray(array))