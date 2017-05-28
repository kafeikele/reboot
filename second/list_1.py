#_*_coding:utf8_*_
#定义一个list
#列表-序列：有序的、可遍历的集合
#    ['a' , 'b' , 'c']
#索引  0     1     2  可以通过索引去访问元素


append 追加元素
count  统计次数
extend 扩展原列表
index 获取索引
insert 插入数据
pop remove 移除一个元素
reverse 反向存储

for example：

list:列表
test_list = [0 ,'str',None,True,[],[1]]
列表中包含的元素有：数字、字符串、布尔值、也可以包含另外一个列表

In [1]: a = ["c", "python", "php", "java", "golang", "html"]

In [2]: a[1]
Out[2]: 'python'

In [3]: a[-1]
Out[3]: 'html'

In [4]: a[:1]
Out[4]: ['c']

In [5]: a[1:5]
Out[5]: ['python', 'php', 'java', 'golang']

In [6]: a[1:]
Out[6]: ['python', 'php', 'java', 'golang', 'html']

In [7]: a[:3]
Out[7]: ['c', 'python', 'php']


In [1]: name_list = ['wxh','wdh','whh']
In [2]: name_list[0]
Out[2]: 'wxh'
In [3]: name_list.append('www')  (添加一个元素)
In [4]: name_list.insert(2,'hhh')   （插入一个元素，在whh的前面）
In [6]: name_list.remove('www')  （删掉一个元素）
In [7]: del name_list[0]
In [11]: name_list.count('wxh')  （统计wxh出现的次数）
Out[11]: 1
In [14]: name_list.index('wxh')   （查找元素）
Out[14]: 0
In [11]: name_list[0] = 'hhh'
In [5]: name_list
Out[5]: ['hhh', 'wdh', 'whh']

In [26]: name_list2 = ['a',1,2,3,4,5,6,7]
In [27]: name_list_new = name_list + name_list2
In [28]: name_list_new
Out[28]: ['wdh', 'whh', 'wxh', 'a', 1, 2, 3, 4, 5, 6, 7]

In [29]: name_list.extend(name_list2)

In [30]: name_list
Out[30]: ['wdh', 'whh', 'wxh', 'a', 1, 2, 3, 4, 5, 6, 7]

In [31]: name_list +=name_list2
In [32]: name_list
Out[32]: ['wdh', 'whh', 'wxh', 'a', 1, 2, 3, 4, 5, 6, 7, 'a', 1, 2, 3, 4, 5, 6, 7]

In [35]: name_list[name_list.index(5):name_list.index(5)+4]
Out[35]: [5, 6, 7, 'a']

In [45]: name_list[1:3]
Out[45]: ['whh', 'wxh']

In [48]: name_list[:5]
Out[48]: ['wdh', 'whh', 'wxh', 'a', 1]  打印0~4

In [50]: name_list[16:]
Out[50]: [5, 6, 7]    打印16到最后

a=range(100)
a[::2]  只取偶数
a[1::2]  只取奇数
In [46]: name_list[1::3]
Out[46]: ['whh', 1, 4, 7, 2, 5] 每隔三个打印


