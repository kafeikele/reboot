#_*_coding:utf8_*_
try:
    可能出错的代码  for example :  1 / 0 ,出错后就不往下执行了，下面的print 'hello'不会执行，不出错就继续执行。
    print 'hello'
except:
    如果出错，就执行，如果不出错，则不执行  print 'error'


try:
    可能出错的代码
except:
    如果出错
finally:
    不管如何都执行