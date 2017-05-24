#encoding:utf-8
#场景：让用户一直输入数字，如果输入stop，则停止输入，打印所有的数字之和
total = 0
value = 0
while  value != 'stop':
    total += int(value)
    value = raw_input("Please input num  you want: ")
print total


