#encoding:utf-8
#场景：让用户一直输入数字，如果输入字符串的时候，则停止输入，打印所有的数字之和
total = 0
value = '0'
while  value !=  value.isalpha():
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
'''