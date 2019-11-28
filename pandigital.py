# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:52:13 2019

@author: pNser

如果一个n位数刚好包含了1至n中所有数字各一次则称它们是全数字（pandigital）的，
例如四位数1324就是1至4全数字的。从键盘上输入一组整数，输出其中的全数字，若找不到则输出“not found”。

"""

def pandigital(nums): 
    
    result =[]
    
    for item in nums:
        temp = []
        for i in range(len(str(item))):
            temp.append(int(str(item)[i]))
        if sorted(temp) == [x for x in range(1,len(str(item))+1)]:
            result.append(item)
                
    return result
    
    
if __name__ == "__main__":

    lst = pandigital(eval(input()))
    if len(lst) != 0:
        for i in range(len(lst)):
            print(lst[i])
    else:
        print('not found')
          