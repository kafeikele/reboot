#_*_coding:utf8_*_
字典：dict
dir(dict)  显示所有的函数
help(dict.fromkeys) 查看帮助

In [3]: name_info = {'name': 'Jack', 'age': '27', 'job': 'Engineer'}
In [4]: print name_info
{'job': 'Engineer', 'age': '27', 'name': 'Jack'}
In [25]: type(name_info)
Out[25]: dict
In [5]: print name_info['name']
Jack

In [6]: name_info['salary'] =3000   （增加）
In [7]: print name_info
{'job': 'Engineer', 'salary': 3000, 'age': '27', 'name': 'Jack'}

In [8]: name_info['job'] ='IT'   （修改）
In [9]: print name_info
{'job': 'IT', 'salary': 3000, 'age': '27', 'name': 'Jack'}

In [10]: name_info.pop('job')  （删除）
Out[10]: 'IT'
In [11]: print name_info
{'salary': 3000, 'age': '27', 'name': 'Jack'}

In [13]: print name_info.items()   转换成列表
[('salary', 3000), ('age', '27'), ('name', 'Jack')]


列表  VS 字典
dict:
     查找和插入的速度极快，不会随着key的增加而增加
     需要占用大量内存，内存消耗多
     key不可变
     默认无序
list:
     查找和插入的时间随着数据的增加而增加
     占用内存小，消耗内存少
     通过下标查询
     有序