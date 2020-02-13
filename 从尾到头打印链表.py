#coding:utf-8
'''
输入一个链表，从尾到头打印链表每个节点的值。
'''

#考点很简单，使用栈来存储从头到位遍历到元素，打印栈中元素即可
class Node():
    def __init__(self,val_=None,next_=None):
        self.val = val_
        self.next = next_

class Solution():
    def inverse_list(self,head):
        if head is None:return None
        result=[]
        while head:
            result.insert(0,head.val)
            head=head.next
        for i in result:
            print(i)

if __name__=='__main__':
    head = Node(1,Node(3,Node(10)))
    Solution().inverse_list(head)
