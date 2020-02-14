#coding:utf-8
'''
输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

#思路，没有算法思想，考的代码能力
class Node():
    def __init__(self,val_=None,next_=None):
        self.val = val_
        self.next = next_

#迭代法
class Solution():
    def Merge(self, node1, node2):
        if node1 is None:return node2
        if node2 is None:return node1
        dummy = Node(0)
        p = dummy
        while node1 and node2: 
            if node1.val < node2.val:
                p.next = node1
                node1 = node1.next
            else:
                p.next = node2
                node2 = node2.next
            p = p.next
        return dummy

#递归   递归比较难理解暂时抛弃

class Solution():
    def Merge(self, node1, node2):
        if node1 is None:return node2
        if node2 is None:return node1
        dummy = Node(0)
        if node1.val < node2.val:
            dummy = node1
            dummy.next = self.Merge(node1.next,node2)
        else:
            dummy = node2
            dummy.next = self.Merge(node1,node2.next) 
        return dummy
    
if __name__=='__main__':
    node1 = Node(1)
    node2 = Node(3)
    node3 = Node(5)
    node1.next = node2
    node2.next = node3

    node4 = Node(2)
    node5 = Node(4)
    node6 = Node(6)
    node4.next = node5
    node5.next = node6

    S = Solution()
    p = S.Merge(node1, node4)
    while p.next:
        p = p.next
        print(p.val)
        
