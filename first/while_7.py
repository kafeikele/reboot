#encoding:utf-8
#场景：让用户一直输入数字，如果输入字符串的时候，则停止输入，打印所有的数字之和
total = 0
value = '0'
while value.isdigit():
    total += int(value)
    value = raw_input("Please input num  you want: ")
    if not value.isdigit():
        break
print total

'''
In [58]: value = '0'
In [59]: value.isalpha()
Out[59]: False
In [60]: value !=  value.isalpha()
Out[60]: True

如果value不等于数字时，break 跳出整个while循环。
if str.isdigit():
为True表示输入的所有字符都是数字，否则，不是全部为数字
str为字符串
str.isalnum() 所有字符都是数字或者字母
str.isalpha() 所有字符都是字母
str.isdigit() 所有字符都是数字
str.islower() 所有字符都是小写
str.isupper() 所有字符都是大写
str.istitle() 所有单词都是首字母大写，像标题
str.isspace() 所有字符都是空白字符、\t、\n、\r

'''