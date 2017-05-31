#_*_coding:utf8_*_
#读取myfile.txt
#输出其内容
#去除该文本的换行
#复制这个文件，把第二行换为wd

handler = open("myfile.txt",'r')
cxt = handler.read()
handler.close()
print cxt
cxt_list = cxt.splitlines()   #列表
print cxt_list

handler = open("myfile.bakkk",'w')
cxt_list[1] = '356'
for line in cxt_list:
    handler.write(line + '\n')
handler.close()