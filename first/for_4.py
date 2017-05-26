#_*_coding:utf8_*_
#场景：遍历一个序列['C','python','js','css','js','html','node']
#统计这个序列中jss出现的次数。
x = 0
chars = ['C','python','js','css','js','html','node']
for i in chars:
#    print i
    if i == 'js':
     x += 1
print x