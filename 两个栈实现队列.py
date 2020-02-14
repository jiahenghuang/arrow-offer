#coding:utf-8
'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''
#题目实战中没什么用，不过是考栈和队列的概念，栈先进去后出来，队列先进去先出来
#思路就是用两个栈，一个栈用来push，另一个栈用来pop，pop前需要将上一个栈的元素push到另外一个栈中，最后一个push进来的再从第二个栈中pop出去

class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def push(self,elem):
        self.stack1.append(elem)
        return self.stack1

    def pop(self):
        if not self.stack1 and not self.stack2:return None
        while self.stack1:
            self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

if __name__=='__main__':    
    P = Solution()
    P.push(10)
    P.push(11)
    P.push(12)
    # import pdb;pdb.set_trace()
    print(P.pop())
    P.push(13)
    print(P.pop())
    print(P.pop())
    print(P.pop())
    print(P.pop())


