#coding:utf-8
#二叉搜索树是什么东西？
#一棵二叉树， 根节点与左右子节点有一直值的大小关系，左子节点小于根节点值，根节点小于右节点值
#值的顺序关系对增删改查有啥改进的地方吗？相对于线性表
#二叉树相当于二分搜索，每一次都把时间降低一倍
#增删改查时间复杂度为O(h),即树的高度

class TreeNode():
    def __init__(self,val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinSearchTree():
    #迭代法
    def find_min(self, root):
        if root is None:return None
        current=root
        while current.left:
            current = current.left
        return current.val
    
    #递归    
    def find_min_recu(self,root):
        if root is None:return None
        if root.left is None:return root.val
        return self.find_min_recu(root.left)

    #递归
    def find_max_recu(self,root):
        if root is None:return None
        if root.right is None:return root.val
        return self.find_max_recu(root.right)

    #迭代
    def find_max(self, root):
        if root is None:return None
        current = root
        while current.right:
            current = current.right
        return current.val
    
    #迭代
    def insert(self, root, data):
        node=TreeNode(data)
        if root is None:
            return root
        current = root
        while True:
            if data < current.val:
                if current.left is None:
                    current.left = node
                    return root
                current = current.left
        
            else:
                if current.right is None:
                    current.right = node
                    return root
                current = current.right
    #递归
    def insert_recu(self, root, data):
        node = TreeNode(data)
        if root is None:return node
        if data < root.val:
            if root.left is None:
                root.left = node
                return root
        if data > root.val:
            if root.right is None:
                root.right = node
                return root
        root = self.insert_recu(root.left,data)
        root = self.insert_recu(root.right,data)
        return root
    
    #迭代
    def search(self, root, data):
        if root is None:return False
        current = root
        while current is not None:
            if data < current.val:
                current = current.left
            elif data > current.val:
                current = current.right
            else:
                return True
        return False
    #递归
    def search_recu(self, root, data):
        if root is None:return False
        current = root
        if current.val == data:
            return True
        return self.search_recu(root.left,data) or self.search_recu(root.right,data)   

if __name__=='__main__':
    bst = BinSearchTree()
    node = TreeNode(7)
    root = node
    for num in (5, 9, 8, 15, 16, 18, 17):
        bst.insert(root,num)
    print(root.right.right.val)
    max_node = bst.search(root,18)
    min_node = bst.search_recu(root,18)
    print(max_node)
    print(min_node)







