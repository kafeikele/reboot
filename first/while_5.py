#encoding:utf-8
#场景：让用户一直输入数字，如果输入stop，则停止输入，打印所有的数字之和/平均数
total = 0
value = 0
i = 0
while  value != 'stop':
    total += int(value)
    value = raw_input("Please input num  you want: ")   #(开始输入，如果没有下面的if语句，不管输入数字还是stop,i 都会+1，)
    if value != "stop":
        i += 1.0
if  i == 0 :
    print "total: %d ; avg: 0" % total
else:
    print total
    print total / i


