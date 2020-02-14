#coding:utf-8
'''
输入两棵二叉树A，B，判断B是不是A的子结构
空树不是任意一个树的子结构
'''

#递归树的套路就是找初始值，把初使返回值定义好，然后只需要循环左子树右子树就行

class TreeNode():
    def __init__(self, val = None, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def HasSubtree(self, node1, node2):
        if node1 is None:return False
        if node1 is None and node2 is None:
            return False
        if node1.val == node2.val:
            return self.contain_tree(node1,node2)
        return self.HasSubtree(node1.left,node2) and self.HasSubtree(node1.right,node2)

    def contain_tree(self, node1, node2):
        if node2 is None: return True
        if node1 is None: return False
        if node1.val != node2.val:return False
        return self.contain_tree(node1.left,node2.left) and self.contain_tree(node1.right,node2.right) 

if __name__=='__main__':
    pRoot1 = TreeNode(8)
    pRoot2 = TreeNode(8)
    pRoot3 = TreeNode(7)
    pRoot4 = TreeNode(9)
    pRoot5 = TreeNode(2)
    pRoot6 = TreeNode(4)
    pRoot7 = TreeNode(7)
    pRoot1.left = pRoot2
    pRoot1.right = pRoot3
    pRoot2.left = pRoot4
    pRoot2.right = pRoot5
    pRoot5.left = pRoot6
    pRoot5.right = pRoot7

    pRoot8 = TreeNode(8)
    pRoot9 = TreeNode(8)
    pRoot10 = TreeNode(7)
    pRoot8.left = pRoot9
    pRoot8.right = pRoot10

    S = Solution()
    print(S.HasSubtree(pRoot1, pRoot8))