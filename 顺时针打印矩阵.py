#coding:utf-8
'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''
# 好灵活的题目
# 采用转秩  打印完成一行之后就将这一行数据删除，然后翻转，然后再打印这一行

def turn(arr):
    '''
    翻转矩阵
    '''
    arr.pop(0)
    if not arr:return None
    if not arr[0]:return None
    m, n = len(arr),len(arr[0])
    newarr=[]
    for j in range(n-1,-1,-1):
        tmp = []
        for i in range(m):
            tmp.append(arr[i][j])
        newarr.append(tmp)
    return newarr

class Solution():
    def print_num(sellf, arr):
        if not arr:return None
        if not arr[0]:return None
        m,n = len(arr),len(arr[0])
        while arr is not None:
            for i in arr[0]:
                print(i)
            arr = turn(arr)


if __name__=='__main__':
    arr = [[ 1,  2,  3,  4],
           [ 5,  6,  7,  8],
           [ 9, 10, 11, 12],
           [13, 14, 15, 16]]
    Solution().print_num(arr)

