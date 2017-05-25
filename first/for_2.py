#_*_coding:utf8_*_
#场景：遍历一个序列['C','python','js','css','js','html','node']
#统计这个序列中jss出现的索引的位置。
chars = ['C','python','js','css','js','html','node']
first_position = 0
for i in range(chars.count('js')):
    new_chars = chars[first_position: ]
    next_position = new_chars.index('js') + 1
    print 'Find: ' ,first_position + new_chars.index('js')
    first_position += next_position


'''
>>> range(1,5) #代表从1到5(不包含5)
[1, 2, 3, 4]
>>> range(1,5,2) #代表从1到5，间隔2(不包含5)
[1, 3]
>>> range(5) #代表从0到5(不包含5)
[0, 1, 2, 3, 4]

再看看list的操作:
L = ['spam', 'Spam', 'SPAM!']
Python 表达式	结果	描述
L[2]	'SPAM!'	读取列表中第三个元素
L[-2]	'Spam'	读取列表中倒数第二个元素
L[1:]	['Spam', 'SPAM!']	从第二个元素开始截取列表，打印索引1到结束
L[1:3]	['Spam', 'SPAM!']	打印索引 1-2

a = range(100)
a[::2]  只打印偶数
a[1::2] 只打印奇数
a[1::3] 每隔三个打印


列表操作包含以下函数:
1、cmp(list1, list2)：比较两个列表的元素
2、len(list)：列表元素个数
3、max(list)：返回列表元素最大值
4、min(list)：返回列表元素最小值
5、list(seq)：将元组转换为列表
列表操作包含以下方法:
1、list.append(obj)：在列表末尾添加新的对象
2、list.count(obj)：统计某个元素在列表中出现的次数
3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
5、list.insert(index, obj)：将对象插入列表
6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
7、list.remove(obj)：移除列表中某个值的第一个匹配项
8、list.reverse()：反向列表中元素
9、list.sort([func])：对原列表进行排序
'''