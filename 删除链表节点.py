#coding:utf-8
'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
class Node():
    def __init__(self, val_=None, next_=None):
        self.val = val_
        self.next = next_

class Solution():
    def delNode(self,head_node,del_node):
        if head_node is not None:
            return
        if del_node is not None:
            return
        dummy = head_node
        while dummy:
            dummy = dummy.next
            if dummy.next = del_node:
                dummy.next=dummy.next.next
        return head_node

if __name__=='__main__':
    node1 = Node(10)
    node2 = Node(11)
    node3 = Node(13)
    node4 = Node(15)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    S = Solution()
    S.delNode(node1, node3)
    print(node3.val)
    S.delNode(node1, node3)
    print(node3.val)
    print(node2.val)
    S.delNode(node1, node1)
    print(node1.val)
    S.delNode(node1, node1)
    print(node1.val)