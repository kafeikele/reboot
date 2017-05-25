#_*_coding:utf8_*_
#场景：遍历一个序列[1,3,4,5,6,12,344,234,435,34534,234,23]
#统计这个序列中的最大值。
num = [1,3,4,5,6,12,344,234,435,34534,234,23]
max_num =  num[0]
for i in num:
    if i > max_num:
        max_num = i
print max_num



