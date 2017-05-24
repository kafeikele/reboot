#encoding:utf-8
for x in range(10):
    if x == 5:
        break
    print x
print "此为分割线"
for y in range(10):
    if y == 5:
        continue
    print y

'''
输出结果：
C:\Python27\python.exe C:/python/reboot/first/break_continue.py
0
1
2
3
4
此为分割线
0
1
2
3
4
6
7
8
9
使用的break循环，所以执行到x==5的时候就跳出了整个for循环，因此print x语句只打到4的时候就终止了
使用了continue跳出本次循环，因此只有在x==5的时候跳出本次循环，接着下次继续，
因此print x语句只有在x==5的时候没有执行到，其它值均执行到了
'''