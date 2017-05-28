#_*_coding:utf8_*_
In [20]: name_set ={1,2,3,4,5,6}
In [21]: name_set
Out[21]: set([1, 2, 3, 4, 5, 6])
In [22]: type(name_set)
Out[22]: set

In [26]: name_set.add(6)  增加
In [27]: name_set
Out[27]: set([1, 2, 3, 4, 5, 6])
In [28]: a = range(10)   列表
In [29]: a
Out[29]: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
In [30]: a = set(a)    把列表转换成集合



In [37]: x = {1,2,3,4}
In [38]: y = {3,4,5,6}
In [39]: x & y   交集
Out[39]: set([3, 4])
In [40]: x | y    并集
Out[40]: set([1, 2, 3, 4, 5, 6])
In [41]: x  -  y   差集
Out[41]: set([1, 2])
In [42]: x ^ y    反差集
Out[42]: set([1, 2, 5, 6])

x = {1,2,3,4}
y = {3,4,5,6}
x & y   求交集
x | y   求并集
x – y    求差集
x ^ y    求反差集
a.issubset(b)  a是b的子集
a.issuperset(b) a是否包含b
