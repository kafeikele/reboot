#encoding:utf-8
#场景：让用户一直输入数字，如果输入stop，则停止输入，打印所有的数字之和
total = 0
value = 0
i = 0
while  value != 'stop':
    value = raw_input("Please input num  you want: ")
    if value != 'stop':
        total += int(value)
        i += 1.0
if i == 0:
    print "total:%d ; avg: 0"
else:
    print total
    print total / i