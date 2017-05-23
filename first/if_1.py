#_*_coding:utf8_*_
'''
if语句基本语法
if 判断条件：
    执行语句……
else：
    执行语句……
'''

'''
if高级语法
if 判断条件1:
    执行语句1……
elif 判断条件2:
    执行语句2……
elif 判断条件3:
    执行语句3……
else:
    执行语句4……
'''
#练习：输入两个人的年龄，判断大小
wdh_age = raw_input('Please input your age: ')
wxh_age = raw_input('Please input your age: ')
if wdh_age > wxh_age :
    print 'wdh_age > wxh_age'
else:
    if wdh_age == wxh_age :
        print 'wdh_age = wxh_age'
    else:
        print 'wdh_age < wxh_age'


if wdh_age > wxh_age :
    print 'wdh_age > wxh_age'
elif wdh_age == wxh_age :
    print 'wdh_age = wxh_age'
else:
     print 'wdh_age < wxh_age'

'''
C:\Python27\python.exe C:/python/reboot/first/if_1.py
Please input your age: 23
Please input your age: 25
wdh_age < wxh_age

'''