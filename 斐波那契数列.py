'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

class Solucion():
    def s(self,n):
        if n==1: return 1
        if n==2: return 1
        if n > 2:
            return self.s(n-2)+self.s(n-1)

if __name__=='__main__':
    solu = Solucion().s(30)
    print(solu)
