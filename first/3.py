#_*_coding:utf8_*_
#字符串格式化  % 占位符
x = "whh"
y = "man"
z = 25
print "I am %s and I am %s and I am a %d years old"  %(x,y,z)

user_tpl = "I am %s and I am a %s and I am %d years old"
print user_tpl % ('wxh' ,'man' ,25)
print user_tpl % (x , y ,z)

# %作为占位符的时候，如果需要转义的话，就再写一个% ， for example
print 'I am 100%% sure that you are %s' % 'wrong'