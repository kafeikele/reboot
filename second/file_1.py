#_*_coding:utf8_*_
#读取myfile.txt
#输出其内容
#去除该文本的换行
#替换其中的字符“reboot”为“hello”
#复制这个文件，把第二行换为wd

handler = open("myfile.txt",'r')
cxt = handler.read()
handler.close()
print cxt
cxt_list = cxt.splitlines()   #列表
print cxt_list

handler = open("myfile.bak",'w')
cxt_list[1] = 'wd '
for line in cxt_list:
    handler.write(line.replace('reboot','hello') + '\n')
#字符串，str_name.replace('替换前的内容'，'替换后的内容')，当替换前的内容在str_name不存在，
#还是输出原字符的内容

handler.close()



