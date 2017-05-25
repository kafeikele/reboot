#encoding:utf-8
#场景：让用户一直输入数字，如果输入stop，则停止输入，打印所有的数字之和/平均数
total = 0
value = 0
i = 0
while  value != 'stop':
    total += int(value)
    value = raw_input("Please input num  you want: ")
    if value != "stop":
        i += 1.0
if  i == 0 :
    print "total: %d ; avg: 0" % total
else:
    print total
    print total / i


