#_*_coding:utf8_*_
msg = "What's your computer'name"
msg.capitalize()首字母大写
msg.lower()   转小写
msg.upper()   转大写
msg.swapcase() 大小写互换
msg.split(' ') 将str转为list,以空格切分
'|'.join(msg)    （以 | 为分隔符把列表转换成字符串）


>>> msg = "What's your computer'name"
>>> msg.find('name')     （从0开始数）
21
>>> print msg[0:6]
What's
>>> msg.upper()  (转成大写)
"WHAT'S YOUR COMPUTER'NAME"
>>> msg.lower()   （转成小写）
"what's your computer'name"
>>> msg += "sanxing"
>>> msg.lower()
"what's your computer's namesanxing"
>>> msg.split()
["what's", 'your', "computer's", 'namesanxing']
>>> msg
"what's your computer's namesanxing"
>>> msg_list = msg.split("'")   以单引号为分割符，把字符串转换成列表
>>> msg_list
['what', 's your computer', 's namesanxing']
>>> '|'.join(msg_list)    （以|为分隔符把列表转换成字符串）
'what|s your computer|s namesanxing'

>>> len(msg)  字符串的长度
34
>>> ord('A')
65
