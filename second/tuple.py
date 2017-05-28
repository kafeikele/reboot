#_*_coding:utf8_*_
元组：tuple 即常量数组
tuple = ('a','b','c','d','e')

In [16]: name = ('wxh',20,'man')
In [19]: name[0:2]
Out[19]: ('wxh', 20)

列表和数组和互相转换
In [6]: a = (1,2,3,4)
In [7]: a
Out[7]: (1, 2, 3, 4)
In [8]: type(a)
Out[8]: tuple

In [11]: a = list(a)
In [12]: type(a)
Out[12]: list
In [13]: a
Out[13]: [1, 2, 3, 4]
In [14]: a = tuple(a)

In [15]: type(a)
Out[15]: tuple
