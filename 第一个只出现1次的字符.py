#coding:utf-8
'''
在一个字符串(1<=字符串长度<=10000，全部由大写字母组成)中找到第一个只出现一次的字符。
'''
class Solution:
    def find_first(self, s):
        s_dict = {}
        for i in s:
            if i not in s_dict:
                s_dict[i] = 1
            else:
                s_dict[i] += 1
        for i in s:
            if s_dict.get(i) > 1:
                return i
        return None


