'''
输入两个链表，找出它们的第一个公共结点。
'''

#首先需要直到公共节点的概念，
#从某个节点开始一直到结束全部都一样到才是公共节点

class Solution:
    def same_node(self,root1, root2):
        length1 = self.get_list_length(root1)
        length2 = self.get_list_length(root2)
        if length1 > length2:
            long_list = root1
            short_list = root2
        else:
            long_list = root2
            short_list = root1
        length_dif = abs(length1-length2)
        while length_dif:
            long_list = long_list.next
            length_dif -= 1
        
        while long_list != None and short_list != None and long_list != short_list:
            long_list = long_list.next
            short_list = short_list.next
        return long_list


    def get_list_length(self,root):
        length = 0
        while root:
            length += 1
            root = root.next
        return length

