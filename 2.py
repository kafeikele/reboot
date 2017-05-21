#_*_coding:utf8_*_
print  'hello world'
print "What your name?"
myname = input()
print "Nice to meet you , " + myname
print "Nice to meet you , too"
print "The length of your name is: "
print len(myname)
print "What is your age?"
myage = input('please input: ')
print "You will be " + str(myage+ 1) + " in  a  year "

'''
raw_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。
而对于 input() ，它希望能够读取一个合法的 python 表达式，
即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
'''

name = raw_input('Please input your name: ')
print "Hello " + name
age = raw_input('Please input your age: ')
print "Oh ,I am " + str(int(age) +1) + " , I am bigger than you "