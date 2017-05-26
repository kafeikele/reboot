#_*_coding:utf8_*_
#场景：让用户一直输入数字，如果输入stop，则停止输入，打印所有的数字之和
total = 0
value = 0
while  True:
    value = raw_input("Please input the num you want: ")
    try:
        value = int(value)
        total += value
    except:
        try:
            if value == "stop":
                break
        except:
            continue
        print "Wrong , Please input num"

print total

'''
输出结果：
C:\Python27\python.exe C:/python/reboot/first/while_8.py
Please input the num you want: 23
Please input the num you want: 34
Please input the num you want: 445
Please input the num you want: sd
Please input num
Please input the num you want: 23
Please input the num you want: stop
Please input num
525

'''