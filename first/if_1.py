#_*_coding:utf8_*_
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