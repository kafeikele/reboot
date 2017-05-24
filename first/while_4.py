#encoding:utf-8
#场景：输入name，不等于空的时候跳出，等于空的时候继续输入
name_1 = ''
while name_1 == '':   #name_1 == '' 输出的是True
    name_1 = raw_input("Please input your name_1: ")
print name_1

name_2 = ''
while not name_2:   #(not name_2 输出的是 True)
#while not name_2 != '':
    name_2 = raw_input("Please input your name_2: ")
print name_2

'''
In [1]: name = ''
In [2]: not name
Out[2]: True

In [3]: not not name
Out[3]: False
In [4]: name = 'abc'
In [5]: not name
Out[5]: False

In [6]: not not name
Out[6]: True

In [17]: a = ''
In [18]: a == 4
Out[18]: False
In [19]: a == ''
Out[19]: True
In [20]: not a
Out[20]: True

In [24]: b = ''
In [25]: b == 'sdfsdfsdf'
Out[25]: False
In [26]: not b == 'sdfdsfds'
Out[26]: True

'''