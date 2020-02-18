#coding:utf-8
'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

# 超级棒的题目，我曾经面试腾讯的时候被考过。我估计很快我又会碰到你
# 类似快排的思想，找pivot，然后分成小于pivot的和大于pivot的
# 有需要额外空间和不需要额外空间两种
# 实现不需要额外空间，需要修改元素在数组中进行做

#思路：
#1）令数组第一个值为pivot，从第二个数开始与pivot进行比较，如果这个数小于pivot，则指针后移
#2）后指针指向最后一个元素，如果这个元素的值大于pivot，则指针前移
#3）当结束并且后指针还在前指针的后面的话，就交换这两个元素
#4）循环1）2）3）直到前指针在后指针后面
#5）将第一个元素与后指针指向的那个元素交换位置，这样后指针所指向的位置就是小于那个元素的位置，记为index，如果index < k则，需要在后指针后面的数组中再找到k-index个元素
#6）如果index>k,则需要在后指针前面位置继续找k个元素

class Solution:
    def find_least_num(self, arr, k):
        if arr is None:return []
        if len(arr) <= k:return arr
        start = 0
        end = len(arr) - 1
        index = self.partition(arr, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.partition(arr, start, end)
            else:
                start = index + 1
                index = self.Partition(arr, start, end)
        output = tinput[:k]
        output.sort()
        return output


    def partition(self,arr, start, end):
        left_rear = start+1
        right_rear = end
        pivot = arr[start]
        while True:
            while arr[left_rear] <= pivot and left_rear < right_rear:
                left_rear += 1
            while arr[right_rear] >= pivot and left_rear < right_rear:
                right_rear -= 1 
            if left_rear >= right_rear:
                break
            else:
                arr[right_rear], arr[left_rear] = arr[left_rear], arr[right_rear]
        arr[right_rear], arr[start] = arr[start], arr[right_rear]
        return right_rear

    #o(nlogk)
    def GetLeastNumbers(self, tinput, k):
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        output = []
        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]     # 最小堆用 return output

if __name__=='__main__':
    tinput = [4,5,1,6,2,7,3,8]
    s = Solution()
    print(s.find_least_num(tinput, 4))
    print(s.GetLeastNumbers(tinput,4))
