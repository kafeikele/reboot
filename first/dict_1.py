#_*_coding:utf8_*_
#场景：每个字符串出现的次数
lists = ['C','js','python','js','css','js','html','node','js','python','js',
 'css','js','html','node','js','python','js','css','js','html','node',
 'css','js','html','node','js','python','js','css','js','html','node','js',
 'python','js','css','js','html','node']

dicts = {}

for strs in lists:
    if strs not in dicts:
        dicts[strs] = 1
    else:
        dicts[strs] += 1
print dicts

'''
C:/python/reboot/first/dict_1.py
{'node': 6, 'C': 1, 'python': 5, 'js': 16, 'html': 6, 'css': 6}

in的用法
In [44]: x = [1, 2, 3, 4, 6]
In [45]: 7 not in x
Out[45]: True
In [46]: 4 in x
Out[46]: True


In [39]: dicts
Out[39]: {'ss': 2, 'sss': 1}
In [41]: a = 'sssss'
In [42]: a not in dicts
Out[42]: True
'''


