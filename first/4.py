#_*_coding:utf8_*_
# 练习：从命令行输入两个数字，打印出两个数字的和
num1 = raw_input('Please input the number you want: ')
num2 = raw_input('Please input the number you want: ')
s = int(num1) + int(num2)
print '%s + %s = %s' %(num1,num2,s)
print '(%s + %s) / 2 = %s' %(num1 , num2 ,s * 1.0 /2)
print num1,num2,s,s*1.0/2

'''
脚本执行结果
C:\Python27\python.exe C:/python/reboot/first/4.py
Please input the number you want: 45
Please input the number you want: 54
45 + 54 = 99
(45 + 54) / 2 = 49.5
45 54 99 49.5
'''