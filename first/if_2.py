#_*_coding:utf8_*_
#如果age_1的值小于age_2 ,则两个值进行替换，age_1始终显示为最大值
age_1 = raw_input('Please input the age_1: ')
age_2 = raw_input('Please input the age_2: ')
if  age_1 < age_2:
    tmp = age_1
    age_1 = age_2
    age_2 = tmp
    print 'age_1:%s age_2:%s' %(age_1,age_2)

'''
输出结果：
C:\Python27\python.exe C:/python/reboot/first/if_2.py
Please input the age_1: 12
Please input the age_2: 13
age_1:13 age_2:12

'''
