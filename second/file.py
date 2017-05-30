#_*_coding:utf8_*_

'''
文件路径：
    绝对路径：完整的路径
    相对路径：当前脚本启动的目录
r 以只读模式打开文件
w 以只写模式打开文件
a 以追加模式打开文件
r+b 以读写模式打开
w+b 以写读模式打开
a+b 以追加及读模式打开


>>> f = file('file.txt','a')
>>> import startup
>>> f.write('second line')
>>> f.write('third line')
>>> f.write('forth line')
>>> f.close()

'''
f = file('myfile.txt','a')
f.write('make:a:test1 \n')
f.write('make:a:test2 \n')
f.write('make:a:test3 \n')
f.close()


#以只读的方式打开文件myfile,for遍历每一行，
#去掉换行符，以冒号为分割，转换成list,并且打印每行。
f = file('myfile.txt','r')    #file()打开小括号里面的这个文件，以只读的模式打开
for line in f.readlines():     #循环这个文件的每一行
        line = line.strip('\n').split(':')   #line.strip('\n') 去掉每行的换行符，split按照冒号分割成一个一个的列表
        print line

#strip去掉换行符，split分开，是对字符串进行修饰
#line = line.strip('\n').split(':') 已经由字符串转换为列表
#还可以对列表进行修饰，取值[0]
# f.write(u'学习python'.encode('utf-8'))
#f.read()是以字符串的形式读取文件
#f.readline是以列表的形式读取文件
#f.seek(0)回到开头
#f.tell()告诉你在这个文本的哪里
#f.flush()强制刷新
#f.truncate(10)  截断10字节以后的，只留10字节
