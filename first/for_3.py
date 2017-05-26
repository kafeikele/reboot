#_*_coding:utf8_*_
#场景：遍历一个序列['C','python','js','css','js','html','node']
#统计这个序列中jss出现的索引的位置。
chars = ['C','python','js','css','js','html','node']
position = 0
for i in range(chars.count('js')):
    if position == 0:
        position = chars.index('js')
    else:
        position = chars.index('js',position+1)
    print position

'''
help(list)
 index(...)
 |      L.index(value, [start, [stop]]) -> integer -- return first index of value.
 |      Raises ValueError if the value is not present.
'''