# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:57:34 2019

@author: 13486
"""

# 三种数据类型


# 元组

a = (1, 2, 3)
#print(a)
#print(a[1])

# 列表
a = [1, 2, 3]
#print(a)
# 增加列表项
#a.append(4)
#print(a)
#print(a[3])
# 更新列表项
#a[2] = 5
#print(a)
#for i in a:
#    print(i)

# 字典
mydict = {'a': 6.18, 'b':'str', 'c':True}
print('A value: %.2f' % mydict['a'])
# 增加字典元素
mydict['a'] = 523
print('A value: %d' % mydict['a'])
print('keys: %s' % mydict.keys())
print('values: %s' % mydict.values())
for key in mydict:
    print(mydict[key])
# 删除特定元素
mydict.pop('a')
print(mydict)
# 删除字典中的全部元素
mydict.clear()
print(mydict)
