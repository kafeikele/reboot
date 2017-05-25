#_*_coding:utf8_*_
total = 0
value = 0
while value != "stop":
    value = raw_input("Please input the num you want: ")
    try:
        value = int(value)
        total += value
    except:
        print "Please input num"
        if value == "stop":
            break
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